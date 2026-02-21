import json
from datetime import datetime
from typing import List

from app.domain.models.card import Card
from app.domain.models.enums import BattleResult, CardOwner
from app.domain.repositories.battle_repository import BattleRepository
from app.domain.models.battle import Battle
from app.infrastructure.cache.redis_client import RedisClient


class RedisBattleRepository(BattleRepository):

    def __init__(self, redis_client: RedisClient):
        self.redis = redis_client

    async def save_many(self, battles: List[Battle]) -> None:
        pipe = await self.redis.pipeline()
        for battle in battles:
            key = self._build_key(battle.player_tag, battle.battle_time)
            battle_dict = {
                "battle_time": battle.battle_time.isoformat(),
                "player_tag": battle.player_tag,
                "opponent_tag": battle.opponent_tag,
                "result": battle.result.value,
                "crowns_for": battle.crowns_for,
                "crowns_against": battle.crowns_against,
                "elixir_leaked": battle.elixir_leaked,
                "cards": [
                    {
                        "name": card.name,
                        "elixir_cost": card.elixir_cost,
                        "level": card.level,
                        "owner": card.owner.value,
                    }
                    for card in battle.cards
                ],
            }
            pipe.set(key, json.dumps(battle_dict), nx=True)

            index_key = self._build_index_key(battle.player_tag)
            score = battle.battle_time.timestamp()
            pipe.zadd(index_key, {key: score})
        await pipe.execute()

    async def get_by_player(self, player_tag: str) -> List[Battle]:
        index_key = self._build_index_key(player_tag)

        keys = await self.redis.zrevrange(index_key, 0, -1)

        if not keys:
            return []

        raw_data_list = await self.redis.mget(keys)
        return self._parse_battles(raw_data_list)

    async def get_recent_by_player(
        self, player_tag: str, limit: int = 30
    ) -> List[Battle]:
        index_key = self._build_index_key(player_tag)
        keys = await self.redis.zrevrange(index_key, 0, limit - 1)

        if not keys:
            return []
        raw_data_list = await self.redis.mget(keys)
        return self._parse_battles(raw_data_list)

    async def delete_by_player(self, player_tag: str) -> None:
        index_key = self._build_index_key(player_tag)
        keys = await self.redis.zrevrange(index_key, 0, -1)
        for key in keys:
            await self.redis.delete(key)
        await self.redis.delete(index_key)

    @staticmethod
    def _build_key(player_tag: str, battle_time: datetime) -> str:
        return f"battle:{player_tag}:{battle_time.isoformat()}"

    @staticmethod
    def _build_index_key(player_tag: str) -> str:
        return f"index:battles:{player_tag}"

    @staticmethod
    def _parse_battles(raw_data_list: list[str]) -> List[Battle]:
        battles = []
        for data in raw_data_list:
            if not data:
                continue
            raw = json.loads(data)
            cards = [
                Card(
                    name=c["name"],
                    elixir_cost=c["elixir_cost"],
                    level=c["level"],
                    owner=CardOwner(c["owner"]),
                )
                for c in raw["cards"]
            ]
            battle = Battle(
                battle_time=datetime.fromisoformat(raw["battle_time"]),
                player_tag=raw["player_tag"],
                opponent_tag=raw["opponent_tag"],
                result=BattleResult(raw["result"]),
                crowns_for=raw["crowns_for"],
                crowns_against=raw["crowns_against"],
                elixir_leaked=raw["elixir_leaked"],
                cards=cards,
            )
            battles.append(battle)
        return battles

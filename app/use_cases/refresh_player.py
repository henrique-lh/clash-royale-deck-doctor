from datetime import datetime
from itertools import chain

from app.domain.models.battle import Battle
from app.domain.models.card import Card
from app.domain.models.enums import BattleResult, CardOwner
from app.domain.repositories.battle_repository import BattleRepository
from app.infrastructure.external.clash_royale.clash_api_client import ClashAPIClient


class RefreshPlayerUseCase:

    def __init__(self, repository: BattleRepository, api_client: ClashAPIClient):
        self.repository = repository
        self.api_client = api_client

    async def execute(self, player_tag: str):

        raw_battles = await self.api_client.get_battle_log(player_tag)

        await self.repository.delete_by_player(player_tag)

        battles = [self._map_battle(b, player_tag) for b in raw_battles]

        await self.repository.save_many(battles)

        return {"player_tag": player_tag, "battles_imported": len(battles)}

    def _map_battle(self, raw: dict, player_tag: str) -> Battle:

        player_data = raw["team"][0]
        opponent_data = raw["opponent"][0]

        result = self._determine_result(player_data["crowns"], opponent_data["crowns"])

        player_cards = []
        opponent_cards = []

        for c in player_data["cards"]:
            if c["name"]  == "Mirror":
                c["elixirCost"] = 0.0
            card = Card(
                name=c["name"],
                elixir_cost=c["elixirCost"],
                level=c["level"],
                owner=CardOwner.PLAYER,
            )
            player_cards.append(card)

        for c in opponent_data["cards"]:
            if c["name"]  == "Mirror":
                c["elixirCost"] = 0.0
            card = Card(
                name=c["name"],
                elixir_cost=c["elixirCost"],
                level=c["level"],
                owner=CardOwner.OPPONENT,
            )
            opponent_cards.append(card)

        cards = list(chain(player_cards, opponent_cards))

        return Battle(
            battle_time=datetime.fromisoformat(raw["battleTime"].replace("Z", "")),
            player_tag=player_tag,
            opponent_tag=opponent_data["tag"],
            result=result,
            crowns_for=player_data["crowns"],
            crowns_against=opponent_data["crowns"],
            elixir_leaked=player_data.get("elixirLeaked", 0.0),
            cards=cards,
        )

    @staticmethod
    def _determine_result(player_crowns, opponent_crowns):
        if player_crowns > opponent_crowns:
            return BattleResult.WIN
        elif player_crowns < opponent_crowns:
            return BattleResult.LOSS
        return BattleResult.DRAW

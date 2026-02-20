from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from app.domain.models.card import Card
from app.domain.models.enums import BattleResult, CardOwner


@dataclass
class Battle:
    battle_time: datetime
    player_tag: str
    opponent_tag: str
    result: BattleResult
    crowns_for: int
    crowns_against: int
    elixir_leaked: float
    cards: List[Card] = field(default_factory=list)

    def player_cards(self) -> List[Card]:
        return [c for c in self.cards if c.owner == CardOwner.PLAYER]

    def opponent_cards(self) -> List[Card]:
        return [c for c in self.cards if c.owner == CardOwner.OPPONENT]

    def average_elixir(self) -> float:
        player_cards = self.player_cards()
        if not player_cards:
            return 0.0
        return sum(c.elixir_cost for c in player_cards) / len(player_cards)

    def is_win(self) -> bool:
        return self.result == BattleResult.WIN

    def is_loss(self) -> bool:
        return self.result == BattleResult.LOSS

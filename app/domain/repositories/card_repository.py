from abc import ABC, abstractmethod
from typing import List

from app.domain.models.card import Card


class CardRepository(ABC):
    """Contract for card persistence layer."""

    @abstractmethod
    def save_many(self, cards: List[Card]) -> None:
        """Persist multiple cards."""
        pass

    @abstractmethod
    def get_by_battle(self, battle_id: str) -> List[Card]:
        """Return cards associated with a battle."""
        pass

    @abstractmethod
    def get_by_player(self, player_tag: str) -> List[Card]:
        """Return all cards used by a player."""
        pass

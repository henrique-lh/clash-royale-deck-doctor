from abc import ABC, abstractmethod
from typing import List

from app.domain.models.battle import Battle


class BattleRepository(ABC):
    """Contract for battle persistence layer."""

    @abstractmethod
    async def save_many(self, battles: List[Battle]) -> None:
        """Persist multiple battles."""
        pass

    @abstractmethod
    async def get_by_player(self, player_tag: str) -> List[Battle]:
        """Return all battles for a given player."""
        pass

    @abstractmethod
    async def get_recent_by_player(
        self,
        player_tag: str,
        limit: int = 30
    ) -> List[Battle]:
        """Return most recent battles for a player."""
        pass

    @abstractmethod
    async def delete_by_player(self, player_tag: str) -> None:
        """Delete battles of a player (used for refresh)."""
        pass

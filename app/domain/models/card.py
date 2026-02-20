from dataclasses import dataclass
from app.domain.models.enums import CardOwner


@dataclass(frozen=True)
class Card:
    name: str
    elixir_cost: float
    level: int
    owner: CardOwner

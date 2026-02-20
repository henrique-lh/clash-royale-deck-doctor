from sqlalchemy import String, Float, Integer, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.base import Base
from app.domain.models.enums import CardOwner


class CardModel(Base):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    battle_id: Mapped[int] = mapped_column(
        ForeignKey("battles.id", ondelete="CASCADE"),
        index=True
    )

    name: Mapped[str] = mapped_column(String(50))
    elixir_cost: Mapped[float] = mapped_column(Float)
    level: Mapped[int] = mapped_column(Integer)
    owner: Mapped[CardOwner] = mapped_column(Enum(CardOwner))

    battle = relationship("BattleModel", back_populates="cards")

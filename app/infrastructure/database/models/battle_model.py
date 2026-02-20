from datetime import datetime
from sqlalchemy import String, Integer, Float, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from app.infrastructure.database.base import Base
from app.domain.models.enums import BattleResult


class BattleModel(Base):
    __tablename__ = "battles"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    player_tag: Mapped[str] = mapped_column(String(20), index=True)
    opponent_tag: Mapped[str] = mapped_column(String(20))

    battle_time: Mapped[datetime] = mapped_column(DateTime, index=True)

    result: Mapped[BattleResult] = mapped_column(Enum(BattleResult))

    crowns_for: Mapped[int] = mapped_column(Integer)
    crowns_against: Mapped[int] = mapped_column(Integer)

    elixir_leaked: Mapped[float] = mapped_column(Float)

    cards: Mapped[List["CardModel"]] = relationship(
        back_populates="battle",
        cascade="all, delete-orphan"
    )

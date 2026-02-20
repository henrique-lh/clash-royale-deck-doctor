from enum import Enum


class BattleResult(str, Enum):
    WIN = "win"
    LOSS = "loss"
    DRAW = "draw"


class CardOwner(str, Enum):
    PLAYER = "player"
    OPPONENT = "opponent"

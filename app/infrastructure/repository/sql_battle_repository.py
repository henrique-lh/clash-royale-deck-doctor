from sqlalchemy.orm import Session

from app.domain.repositories.battle_repository import BattleRepository
from app.domain.models.battle import Battle
from app.infrastructure.database.models.battle_model import BattleModel
from app.infrastructure.database.mappers.battle_mapper import BattleMapper


class SQLBattleRepository(BattleRepository):

    def __init__(self, db: Session):
        self.db = db

    def save_many(self, battles: list[Battle]) -> None:
        models = [BattleMapper.to_model(b) for b in battles]
        self.db.add_all(models)
        self.db.commit()

    def get_by_player(self, player_tag: str) -> list[Battle]:
        models = (
            self.db.query(BattleModel)
            .filter(BattleModel.player_tag == player_tag)
            .all()
        )
        return [BattleMapper.to_domain(m) for m in models]

    def get_recent_by_player(self, player_tag: str, limit: int = 30):
        models = (
            self.db.query(BattleModel)
            .filter(BattleModel.player_tag == player_tag)
            .order_by(BattleModel.battle_time.desc())
            .limit(limit)
            .all()
        )
        return [BattleMapper.to_domain(m) for m in models]

    def delete_by_player(self, player_tag: str) -> None:
        self.db.query(BattleModel)\
            .filter(BattleModel.player_tag == player_tag)\
            .delete()
        self.db.commit()

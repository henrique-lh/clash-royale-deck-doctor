from app.domain.models.battle import Battle
from app.domain.models.card import Card
from app.infrastructure.database.models.battle_model import BattleModel
from app.infrastructure.database.models.card_model import CardModel


class BattleMapper:

    @staticmethod
    def to_domain(model: BattleModel) -> Battle:
        cards = [
            Card(
                name=c.name,
                elixir_cost=c.elixir_cost,
                level=c.level,
                owner=c.owner
            )
            for c in model.cards
        ]

        return Battle(
            battle_time=model.battle_time,
            player_tag=model.player_tag,
            opponent_tag=model.opponent_tag,
            result=model.result,
            crowns_for=model.crowns_for,
            crowns_against=model.crowns_against,
            elixir_leaked=model.elixir_leaked,
            cards=cards
        )

    @staticmethod
    def to_model(domain: Battle) -> BattleModel:
        battle_model = BattleModel(
            battle_time=domain.battle_time,
            player_tag=domain.player_tag,
            opponent_tag=domain.opponent_tag,
            result=domain.result,
            crowns_for=domain.crowns_for,
            crowns_against=domain.crowns_against,
            elixir_leaked=domain.elixir_leaked,
        )

        battle_model.cards = [
            CardModel(
                name=c.name,
                elixir_cost=c.elixir_cost,
                level=c.level,
                owner=c.owner,
            )
            for c in domain.cards
        ]

        return battle_model

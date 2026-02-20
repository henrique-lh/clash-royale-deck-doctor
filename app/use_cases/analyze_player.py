from app.domain.models.stats import BattleStats
from app.domain.repositories.battle_repository import BattleRepository
from app.domain.services.battle_analysis_service import analyze_battles
from app.domain.services.deck_classifier import classify_deck
from app.domain.services.diagnosis_engine import generate_diagnosis_report
from app.domain.services.matchup_detector import detect_common_cards
from app.infrastructure.external.ollama.ollama_client import OllamaClient


class AnalyzePlayerUseCase:

    def __init__(self, repository: BattleRepository):
        self.repository = repository

    def execute(self, player_tag: str, ollama_client: OllamaClient):

        battles = self.repository.get_recent_by_player(player_tag)

        stats = BattleStats(**analyze_battles(battles))

        deck_type = classify_deck(stats.avg_elixir)

        matchups = detect_common_cards(battles)

        diagnosis = generate_diagnosis_report(battles, stats, deck_type, matchups, ollama_client)

        return {
            "stats": stats,
            "matchups": matchups,
            "diagnosis": diagnosis
        }

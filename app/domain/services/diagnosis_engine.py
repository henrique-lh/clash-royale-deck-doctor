from typing import List, Dict

from app.domain.models.battle import Battle
from app.domain.models.stats import BattleStats
from app.infrastructure.external.ollama.ollama_client import OllamaClient


BUILDINGS = [
    "Cannon",
    "Tesla",
    "Mortar",
    "Goblin Cage",
    "Goblin Hut",
    "Tombstone",
    "Inferno Tower",
    "Bomb Tower",
    "Barbarian Hut",
    "Elixir Collector",
    "X-Bow",
    "Goblin Drill",
]


def _has_building(battles: List[Battle]) -> bool:
    if not battles:
        return False

    sample_deck = battles[0].player_cards()

    return any(card.name in BUILDINGS for card in sample_deck)


async def generate_diagnosis_report(
    battles: List[Battle],
    stats: BattleStats,
    deck_type: str,
    matchups: List[Dict],
    current_deck: List[Dict],
    ollama_client: OllamaClient,
) -> Dict:

    generic_diagnosis = []
    llm_input_diagnosis = []

    if stats.winrate < 45:
        generic_diagnosis.append(f"Seu winrate está abaixo de 45%.")
        llm_input_diagnosis.append(
            f"user win rate is below 45%. Current win rate: {stats.winrate}%"
        )

    if stats.avg_elixir_leaked > 15:
        generic_diagnosis.append("Você está vazando muito elixir.")
        llm_input_diagnosis.append(
            f"user elixir leak is above 15%. Current elixir leak: {stats.avg_elixir_leaked}"
        )

    if not _has_building(battles):
        generic_diagnosis.append("Seu deck não possui estrutura defensiva.")
        llm_input_diagnosis.append("user deck does not have defensive structure.")

    if matchups:
        top_problems = ",".join(m["card"] for m in matchups[:5])
        generic_diagnosis.append(
            f"Dificuldade contra decks que possuem as cartas {top_problems}."
        )

        llm_input_diagnosis.append(
            f"difficulty against decks that have: {matchups[:5]}"
        )

    recommendations = await ollama_client.generate_recommendation(
        llm_input_diagnosis, current_deck
    )

    return {
        "deck_type": deck_type,
        "problems": generic_diagnosis,
        "recommendations": recommendations,
    }

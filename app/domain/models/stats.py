from dataclasses import dataclass


@dataclass
class BattleStats:
    total_battles: int
    wins: int
    losses: int
    winrate: float
    avg_elixir: float
    avg_elixir_leaked: float

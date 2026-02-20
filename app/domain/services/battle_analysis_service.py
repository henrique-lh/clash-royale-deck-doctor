from statistics import mean

from app.domain.models.battle import Battle


def analyze_battles(battles: list[Battle]) -> dict:

    if not battles:
        return {
            "total_battles": 0,
            "wins": 0,
            "losses": 0,
            "winrate": 0.0,
            "avg_elixir": 0.0,
            "avg_elixir_leaked": 0.0,
        }

    total = len(battles)

    wins = sum(1 for b in battles if b.is_win())
    losses = sum(1 for b in battles if b.is_loss())

    winrate = wins / total * 100

    avg_elixir = mean(b.average_elixir() for b in battles)

    avg_leak = mean(b.elixir_leaked for b in battles)

    return {
        "total_battles": total,
        "wins": wins,
        "losses": losses,
        "winrate": round(winrate, 2),
        "avg_elixir": round(avg_elixir, 2),
        "avg_elixir_leaked": round(avg_leak, 2),
    }

def classify_deck(avg_elixir: float) -> str:
    if avg_elixir < 3.0:
        return "Cycle"
    elif avg_elixir <= 3.8:
        return "Control"
    return "Beatdown"

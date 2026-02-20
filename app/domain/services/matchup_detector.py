from collections import Counter

from app.domain.models.battle import Battle


def detect_common_cards(battles: list[Battle]) -> list[dict]:

    losses = [b for b in battles if b.is_loss()]

    counter = Counter()

    for battle in losses:
        for card in battle.opponent_cards():
            counter[card.name] += 1

    most_common = counter.most_common(10)

    return [
        {"card": name, "appearances": count}
        for name, count in most_common
    ]

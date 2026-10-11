"""Problem 6.27: five counts over a deck, checked on a small deck before being trusted.
"""
from itertools import combinations

from dmkit.combin import combinations_count

RANKS = list(range(1, 14))
SUITS = list("cdhs")
DECK = [(r, s) for r in RANKS for s in SUITS]


def flushes(deck, ranks, suits, size):
    """Hands whose cards all share a suit."""
    return suits * combinations_count(ranks, size)


def one_pair(deck, ranks, suits, size):
    """Hands with exactly two cards of one rank and no other repeat, at size 5."""
    return (ranks * combinations_count(suits, 2)
            * combinations_count(ranks - 1, size - 2) * suits ** (size - 2))


small_ranks, small_suits, size = 5, 3, 3
small = [(r, s) for r in range(small_ranks) for s in range(small_suits)]
built = list(combinations(small, size))
built_flushes = [h for h in built if len(set(s for _, s in h)) == 1]
print(f"a small deck: {small_ranks} ranks and {small_suits} suits, {len(small)} cards")
print(f"{'collection':>28} {'by the rule':>12} {'by building':>12} {'agree':>7}")
print(f"{'all hands of 3':>28} {combinations_count(len(small), size):>12} "
      f"{len(built):>12} "
      f"{str(combinations_count(len(small), size) == len(built)):>7}")
rule = flushes(small, small_ranks, small_suits, size)
print(f"{'hands all of one suit':>28} {rule:>12} {len(built_flushes):>12} "
      f"{str(rule == len(built_flushes)):>7}")
print()
print(f"the full deck: {len(DECK)} cards")
print(f"{'hands of 5':>28} {combinations_count(len(DECK), 5):>14}")
print(f"{'all of one suit':>28} {flushes(DECK, 13, 4, 5):>14}")
print(f"{'exactly one pair':>28} {one_pair(DECK, 13, 4, 5):>14}")
print()
share = flushes(DECK, 13, 4, 5) / combinations_count(len(DECK), 5)
print(f"one hand in {1 / share:.0f} is all of one suit.")

"""The same predicate, three domains, three different verdicts."""
from dmkit.proof import for_all


def has_a_square_root(n):
    """True when n is a perfect square among the integers."""
    root = int(n ** 0.5)
    return root * root == n or (root + 1) ** 2 == n


domains = [
    ("the squares 0, 1, 4, 9, 16", [0, 1, 4, 9, 16]),
    ("the integers 0 to 4", list(range(5))),
    ("the integers 0 to 20", list(range(21))),
]
print("claim: every member of the domain is a perfect square")
print()
print(f"{'domain':>30} {'members':>9} {'holds':>7}")
for name, dom in domains:
    print(f"{name:>30} {len(dom):>9} {str(for_all(has_a_square_root, dom)):>7}")

"""Problem 5.27: the first size at which a formula and its collection part company."""
from itertools import combinations, permutations, product


def first_disagreement(formula, build, sizes):
    """The smallest size where the formula's answer differs from the built collection.
    """
    for n in sizes:
        built = len(list(build(n)))
        if formula(n) != built:
            return n, formula(n), built
    return None, None, None


checks = [
    ("subsets of n, correct", lambda n: 2 ** n,
     lambda n: (c for k in range(n + 1) for c in combinations(range(n), k))),
    ("subsets of n, off by one", lambda n: 2 ** n - 1,
     lambda n: (c for k in range(n + 1) for c in combinations(range(n), k))),
    ("orderings of n, correct", lambda n: __import__("math").factorial(n),
     lambda n: permutations(range(n))),
    ("orderings of n, using n**n", lambda n: n ** n,
     lambda n: permutations(range(n))),
    ("pairs from n, correct", lambda n: n * (n - 1) // 2,
     lambda n: combinations(range(n), 2)),
    ("pairs from n, forgetting the half", lambda n: n * (n - 1),
     lambda n: combinations(range(n), 2)),
    ("strings of length 3 over n", lambda n: n ** 3,
     lambda n: product(range(n), repeat=3)),
]
print(f"{'formula':>36} {'first size that differs':>24} {'said':>8} {'built':>8}")
for name, formula, build in checks:
    n, said, built = first_disagreement(formula, build, range(0, 8))
    where = "none in 0..7" if n is None else str(n)
    print(f"{name:>36} {where:>24} {str(said):>8} {str(built):>8}")

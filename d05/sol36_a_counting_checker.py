"""Problem 5.25: one checker that runs a formula against the collection it claims to
size."""
from itertools import combinations, permutations, product

from dmkit.counting import enumerate_check, report_count


def check_over_sizes(name, formula, build, sizes):
    """Run one formula against one builder across a range of sizes, and report each row.
    """
    rows = []
    for n in sizes:
        result = enumerate_check(formula(n), lambda n=n: build(n), f"{name}, n = {n}")
        rows.append(result)
        print(report_count(result))
    return all(r["agree"] for r in rows)


print(f"{'collection':>34} {'by the rule':>12} {'by building':>12}  verdict")
all_ok = []
all_ok.append(check_over_sizes(
    "strings of length n over 3",
    lambda n: 3 ** n,
    lambda n: ["".join(t) for t in product("abc", repeat=n)],
    range(0, 6)))
all_ok.append(check_over_sizes(
    "orderings of n items",
    lambda n: __import__("math").factorial(n),
    lambda n: list(permutations(range(n))),
    range(0, 7)))
all_ok.append(check_over_sizes(
    "two-member subsets of n",
    lambda n: n * (n - 1) // 2,
    lambda n: list(combinations(range(n), 2)),
    range(2, 8)))
print()
print(f"every formula agreed with its collection at every size: {all(all_ok)}")

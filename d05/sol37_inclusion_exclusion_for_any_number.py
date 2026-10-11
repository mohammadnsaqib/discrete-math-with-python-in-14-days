"""Problem 5.26: the alternation for any number of groups, checked against the union."""
from itertools import combinations

from dmkit.counting import enumerate_check, inclusion_exclusion, report_count


def by_hand(groups):
    """The same count written out term by term, so the alternation is visible.

    Each term is a sum over subsets of one size. The sign alternates with the size, and
    the routine returns the terms as well as the total so the book can print them.
    """
    terms = []
    for k in range(1, len(groups) + 1):
        subtotal = 0
        for chosen in combinations(groups, k):
            shared = set(chosen[0])
            for g in chosen[1:]:
                shared &= set(g)
            subtotal += len(shared)
        terms.append(((-1) ** (k + 1) * subtotal, k))
    return sum(t for t, _ in terms), terms


upto = list(range(1, 1001))
divisors = (2, 3, 5, 7, 11)
groups = [[n for n in upto if n % d == 0] for d in divisors]

print(f"{'groups':>8} {'subsets walked':>16} {'the terms, by size':>34} {'total':>8}")
for k in range(1, len(groups) + 1):
    total, terms = by_hand(groups[:k])
    print(f"{k:>8} {2 ** k - 1:>16} "
          f"{' '.join(f'{t:+d}' for t, _ in terms):>34} {total:>8}")
print()
print(f"{'collection':>34} {'by the rule':>12} {'by building':>12}  verdict")
for k in range(1, len(groups) + 1):
    print(report_count(enumerate_check(
        inclusion_exclusion(*groups[:k]),
        lambda k=k: sorted(set().union(*[set(g) for g in groups[:k]])),
        f"divisible by one of the first {k}")))
print()
print(f"{'divisors':>34} {'divisible by none':>18}")
for k in range(1, len(groups) + 1):
    survivors = [n for n in upto if all(n % d for d in divisors[:k])]
    print(f"{str(divisors[:k]):>34} {len(survivors):>18}")

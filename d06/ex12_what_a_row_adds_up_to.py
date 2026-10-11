"""Two sums over one row, and what each of them counts."""
from dmkit.combin import binomial, pascal_row
from dmkit.sets import power_set

print(f"{'n':>4} {'the row':>34} {'sum':>8} {'2**n':>8} {'alternating sum':>17}")
for n in range(0, 8):
    row = pascal_row(n)
    alternating = sum((-1) ** k * row[k] for k in range(n + 1))
    print(f"{n:>4} {str(row):>34} {sum(row):>8} {2 ** n:>8} {alternating:>17}")
print()
n = 4
subsets = power_set(set(range(n)))
by_size = {k: [s for s in subsets if len(s) == k] for k in range(n + 1)}
print(f"the {len(subsets)} subsets of a {n}-member set, by size:")
for k in sorted(by_size):
    print(f"   size {k}: {len(by_size[k])} of them, and binomial({n}, {k}) is "
          f"{binomial(n, k)}")

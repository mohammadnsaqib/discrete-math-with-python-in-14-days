"""Problem 6.26: one row of the triangle by three routes that share no arithmetic."""
from itertools import combinations
from math import comb

from dmkit.combin import pascal_by_addition, pascal_row


def by_counting(n):
    """The row built by listing the subsets of each size and measuring each list."""
    items = list(range(n))
    return [len(list(combinations(items, k))) for k in range(n + 1)]


print(f"{'n':>4} {'product = sum':>14} {'sum = library':>14} "
      f"{'library = built list':>21} {'row total':>11}")
for n in range(0, 12):
    multiplied = pascal_row(n)
    added = pascal_by_addition(n)
    library = [comb(n, k) for k in range(n + 1)]
    built = str(library == by_counting(n)) if n <= 9 else "not built"
    print(f"{n:>4} {str(multiplied == added):>14} {str(added == library):>14} "
          f"{built:>21} {sum(multiplied):>11}")
print()
print(f"row 12: {pascal_row(12)}")
print(f"and it adds to {sum(pascal_row(12))}, which is 2**12 = {2 ** 12}")

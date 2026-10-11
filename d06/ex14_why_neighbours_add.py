"""The addition in the triangle is a proof by cases, and the cases can be listed."""
from itertools import combinations

from dmkit.combin import binomial

n, k = 5, 2
items = list("abcde")
last = items[-1]
chosen = [set(c) for c in combinations(items, k)]
with_last = [c for c in chosen if last in c]
without_last = [c for c in chosen if last not in c]

print(f"the {len(chosen)} ways to choose {k} from {items}")
print(f"   containing {last}     : {len(with_last)}")
print(f"   not containing {last} : {len(without_last)}")
print()
print(f"binomial({n - 1}, {k - 1}) is {binomial(n - 1, k - 1)} "
      f"and binomial({n - 1}, {k}) is {binomial(n - 1, k)}")
print(f"their sum is {binomial(n - 1, k - 1) + binomial(n - 1, k)} "
      f"and binomial({n}, {k}) is {binomial(n, k)}")
print()
print(f"{'n':>4} {'k':>4} {'above left':>12} {'above right':>13} {'sum':>8} "
      f"{'binomial(n, k)':>16} {'agree':>7}")
for n in range(1, 8):
    for k in range(1, n):
        left, right = binomial(n - 1, k - 1), binomial(n - 1, k)
        print(f"{n:>4} {k:>4} {left:>12} {right:>13} {left + right:>8} "
              f"{binomial(n, k):>16} {str(left + right == binomial(n, k)):>7}")

"""How many subsets of each size, counted by building them."""
from dmkit.sets import power_set

print(f"{'n':>4} " + " ".join(f"{'k=' + str(k):>6}" for k in range(7))
      + f" {'total':>8}")
for n in range(0, 7):
    subsets = power_set(set(range(1, n + 1)))
    counts = [sum(1 for s in subsets if len(s) == k) for k in range(7)]
    print(f"{n:>4} " + " ".join(f"{c:>6}" for c in counts)
          + f" {len(subsets):>8}")

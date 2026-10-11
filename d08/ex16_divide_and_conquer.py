"""A recurrence that splits a problem rather than shrinking it by one."""
from dmkit.recur import divide_conquer

print(f"{'method':>34} {'the recurrence':>30}")
print(f"{'binary search':>34} {'T(n) = T(n/2) + 1':>30}")
print(f"{'merge sort':>34} {'T(n) = 2*T(n/2) + n':>30}")
print(f"{'a three-way split':>34} {'T(n) = 3*T(n/2) + n':>30}")
print()
methods = [("binary search", 1, 2, lambda n: 1),
           ("merge sort", 2, 2, lambda n: n),
           ("three-way split", 3, 2, lambda n: n)]
sizes = [2 ** k for k in range(0, 11)]
print(f"{'size':>8} " + " ".join(f"{name:>18}" for name, _, _, _ in methods))
costs = {name: divide_conquer(s, f, extra, 1, 1024)
         for name, s, f, extra in methods}
for size in sizes:
    row = [f"{costs[name][size]}" for name, _, _, _ in methods]
    print(f"{size:>8} " + " ".join(f"{v:>18}" for v in row))
print()
print("only powers of two appear, because those "
      "are the sizes where halving is exact and")
print("the recurrence says anything at all. Sizes "
      "between them are interpolated by every")
print("textbook and by nothing here.")
print()
print(f"{'size':>8} {'merge sort cost':>18} {'n log2 n':>12} {'ratio':>8}")
for size in (8, 64, 512, 1024):
    from math import log2
    predicted = size * log2(size)
    print(f"{size:>8} {costs['merge sort'][size]:>18} {predicted:>12.0f} "
          f"{costs['merge sort'][size] / predicted:>8.4f}")

"""Two integers are congruent when they leave the same remainder."""
from dmkit.crypto import congruent

print(f"{'a':>6} {'b':>6} {'m':>4} {'a - b':>7} {'m divides it':>14} "
      f"{'same remainder':>16} {'agree':>7}")
for a, b, m in ((17, 5, 12), (17, 5, 6), (-3, 9, 12), (100, 2, 7), (0, 12, 12),
                (-7, 5, 12), (14, 14, 5)):
    same = a % m == b % m
    print(f"{a:>6} {b:>6} {m:>4} {a - b:>7} {str((a - b) % m == 0):>14} "
          f"{str(same):>16} {str(congruent(a, b, m) == same):>7}")
print()
m = 7
groups = {}
for a in range(-7, 15):
    groups.setdefault(a % m, []).append(a)
print(f"the integers -7 to 14 by their remainder modulo {m}:")
for r in sorted(groups):
    print(f"   {r}: {groups[r]}")
print()
bad = [(a, b, m) for m in range(1, 15) for a in range(-20, 21) for b in range(-20, 21)
       if congruent(a, b, m) != (a % m == b % m)]
print(f"triples where the two definitions differ: {len(bad)}")

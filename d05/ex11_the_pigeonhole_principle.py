"""If there are more items than holes, some hole has two."""
from dmkit.counting import pigeonhole

print(f"{'items':>8} {'holes':>8} {'some hole has at least':>24}")
for items, holes in ((3, 2), (10, 9), (13, 12), (367, 366), (100, 7), (5, 5), (4, 9)):
    print(f"{items:>8} {holes:>8} {pigeonhole(items, holes):>24}")
print()
remainders = {}
for n in range(1, 9):
    remainders.setdefault(n % 7, []).append(n)
print("the numbers 1 to 8 sorted by their remainder on division by 7:")
for r in sorted(remainders):
    print(f"   remainder {r}: {remainders[r]}")
print()
crowded = [r for r, group in remainders.items() if len(group) > 1]
print(f"remainders holding more than one number: {crowded}")

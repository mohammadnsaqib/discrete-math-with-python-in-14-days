"""A set whose members are sets, and the counting that goes with it."""
from dmkit.sets import as_text, power_set

base = {1, 2, 3}
subsets = power_set(base)
print(f"the base set        : {as_text(base)}, {len(base)} members")
print(f"its subsets         : {len(subsets)}")
for s in subsets:
    print(f"   {as_text(s)}")
print()
by_size = {}
for s in subsets:
    by_size.setdefault(len(s), []).append(s)
print(f"{'size':>6} {'how many':>10}")
for k in sorted(by_size):
    print(f"{k:>6} {len(by_size[k]):>10}")
print()
print(f"the sizes add to {sum(len(v) for v in by_size.values())}, which is 2 to the "
      f"power {len(base)}.")
print("Day 6 gives each row of that table a name and a formula.")

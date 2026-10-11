"""The power set doubles, and the reason is Day 1's reason."""
from dmkit.sets import as_text, power_set

print(f"{'members':>9} {'subsets':>10} {'built':>8}")
for n in range(0, 13):
    base = set(range(1, n + 1))
    built = len(power_set(base)) if n <= 12 else None
    print(f"{n:>9} {2 ** n:>10} {built:>8}")
print()
base = {1, 2, 3}
print("each subset is one choice of in-or-out "
      "per member, so a subset IS an assignment:")
for s in power_set(base):
    pattern = "".join("1" if x in s else "0" for x in sorted(base))
    print(f"   {pattern}  ->  {as_text(s)}")

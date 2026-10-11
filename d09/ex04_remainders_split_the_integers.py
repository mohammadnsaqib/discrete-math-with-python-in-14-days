"""The remainder sorts every integer into one of b groups, and never into two."""
from dmkit.number import division_algorithm

b = 5
groups = {}
for a in range(-7, 18):
    _, r = division_algorithm(a, b)
    groups.setdefault(r, []).append(a)

print(f"the integers -7 to 17, sorted by their remainder on division by {b}:")
for r in sorted(groups):
    print(f"   remainder {r}: {groups[r]}")
print()
sizes = sorted(set(len(g) for g in groups.values()))
every = sorted(a for g in groups.values() for a in g)
print(f"groups: {len(groups)}, group sizes present: {sizes}")
print(f"every integer appears once: {every == list(range(-7, 18))}")
print()
print(f"{'b':>4} {'groups':>8} {'how many of 1 to 30 in each':>34}")
for b in (2, 3, 5, 7):
    counts = [len([a for a in range(1, 31) if a % b == r]) for r in range(b)]
    print(f"{b:>4} {b:>8} {str(counts):>34}")

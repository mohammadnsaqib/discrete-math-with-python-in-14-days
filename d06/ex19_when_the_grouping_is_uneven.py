"""The division only works when every group has the same size, and here is one that does
not."""
from itertools import permutations

from dmkit.combin import distinct_arrangements, factorial_of, multiset_permutations

for word in ("aab", "banana"):
    everything = ["".join(p) for p in permutations(word)]
    groups = {}
    for arrangement in everything:
        groups.setdefault(arrangement, 0)
        groups[arrangement] += 1
    sizes = sorted(set(groups.values()))
    counts = [word.count(ch) for ch in sorted(set(word))]
    divisor = 1
    for c in counts:
        divisor *= factorial_of(c)
    print(f"word '{word}'")
    print(f"   arrangements produced : {len(everything)}")
    print(f"   distinct words        : {len(groups)}")
    print(f"   group sizes present   : {sizes}")
    print(f"   the divisor used      : {divisor}")
    print(f"   the rule gives        : {multiset_permutations(counts)}")
    print()
# AND ONE GROUPING THAT IS NOT EVEN, for contrast. The distinct arrangements of 'aab'
# are grouped by their first letter, and the groups come out at different sizes.
by_first = {}
for arrangement in sorted(set("".join(p) for p in permutations("aab"))):
    by_first.setdefault(arrangement[0], []).append(arrangement)
print("the distinct arrangements of 'aab', grouped by first letter:")
for ch in sorted(by_first):
    print(f"   starting {ch}: {by_first[ch]}")
sizes = sorted(len(g) for g in by_first.values())
print(f"   group sizes: {sizes}")
print(f"   groups: {len(by_first)}, words: {sum(sizes)}, "
      f"words over groups: {sum(sizes) / len(by_first):.4f}")

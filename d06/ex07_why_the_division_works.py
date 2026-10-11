"""The division in the combination formula, shown rather than asserted."""
from itertools import combinations, permutations

from dmkit.combin import combinations_count, factorial_of, permutations_count

letters = list("abcd")
k = 3
groups = {}
for arrangement in permutations(letters, k):
    groups.setdefault(tuple(sorted(arrangement)), []).append("".join(arrangement))

print(f"every ordered choice of {k} from {letters}, grouped by which items were "
      f"chosen:")
for selection in sorted(groups):
    print(f"   {''.join(selection)} : {groups[selection]}")
print()
sizes = sorted(set(len(g) for g in groups.values()))
print(f"group sizes present: {sizes}, and {k}! is {factorial_of(k)}")
print(f"groups: {len(groups)}, ordered choices: {permutations_count(len(letters), k)}")
print(f"the formula gives {combinations_count(len(letters), k)}")

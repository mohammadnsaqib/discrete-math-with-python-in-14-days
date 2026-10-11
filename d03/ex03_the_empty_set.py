"""One empty set, and the two ways it turns up."""
from dmkit.sets import as_text, power_set

empty = set()
print(f"the empty set          : {as_text(empty)}, with {len(empty)} members")
print(f"a set containing it    : has {len({frozenset()})} member, which is a set")
print()
print(f"   empty is a subset of {{1,2,3}} : {empty <= {1, 2, 3}}")
print(f"   empty is a member of {{1,2,3}} : {frozenset() in {1, 2, 3}}")
print(f"   empty is a subset of empty   : {empty <= empty}")
print()
subsets = power_set(empty)
print(f"the power set of the empty set has {len(subsets)} member: "
      f"{[as_text(s) for s in subsets]}")
subsets2 = power_set({1})
print(f"the power set of a one-member set has {len(subsets2)}: "
      f"{[as_text(s) for s in subsets2]}")

"""A relation with all three properties splits its domain into groups."""
from dmkit.sets import (equivalence_classes, is_reflexive, is_symmetric,
                        is_transitive)

dom = set(range(0, 15))
same_remainder = {(a, b) for a in dom for b in dom if a % 4 == b % 4}

print(f"relation: a and b leave the same remainder on division by 4")
print(f"   reflexive  : {is_reflexive(same_remainder, dom)}")
print(f"   symmetric  : {is_symmetric(same_remainder)}")
print(f"   transitive : {is_transitive(same_remainder)}")
print()
classes = equivalence_classes(same_remainder, dom)
print(f"it splits {len(dom)} members into {len(classes)} groups:")
for group in classes:
    print(f"   {group}")
print()
sizes = [len(g) for g in classes]
print(f"the group sizes are {sizes} and they add to {sum(sizes)}, which is the whole")

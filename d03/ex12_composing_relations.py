"""Two relations applied in turn, and the pairs that survive."""
from dmkit.sets import compose

parent = [("ann", "bob"), ("bob", "cal"), ("ann", "dee"), ("dee", "eve")]
grandparent = compose(parent, parent)
great = compose(grandparent, parent)

print(f"parent      : {parent}")
print(f"grandparent : {grandparent}")
print(f"great-grand : {great}")
print()
print(f"{'relation':>14} {'pairs':>7}")
for name, rel in (("parent", parent), ("grandparent", grandparent),
                  ("great-grand", great)):
    print(f"{name:>14} {len(rel):>7}")

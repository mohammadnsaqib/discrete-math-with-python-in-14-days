"""A binary tree with an ordering rule, and what the rule buys."""
from dmkit.tree import BinaryTree, inorder, insert

values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
tree = None
for v in values:
    tree = insert(tree, v)

print(f"inserted in this order: {values}")
print(f"size   : {tree.size()}")
print(f"height : {tree.height()}")
print(f"inorder: {inorder(tree)}")
print(f"sorted : {sorted(values)}")
print(f"they match: {inorder(tree) == sorted(values)}")
print()
print(f"{'insertion order':>34} {'height':>8} {'inorder is sorted':>19}")
for order in ([8, 3, 10, 1, 6, 14, 4, 7, 13], sorted(values),
              sorted(values, reverse=True), [6, 3, 10, 1, 4, 8, 14, 7, 13]):
    t = None
    for v in order:
        t = insert(t, v)
    print(f"{str(order):>34} {t.height():>8} "
          f"{str(inorder(t) == sorted(values)):>19}")

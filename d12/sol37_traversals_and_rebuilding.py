"""Problem 12.26: the three walks, and what any two of them fix."""
from itertools import permutations

from dmkit.tree import BinaryTree, inorder, insert, postorder, preorder


def rebuild_from_pre_in(pre, ino):
    """The tree with the given preorder and inorder walks."""
    if not pre:
        return None
    cut = ino.index(pre[0])
    return BinaryTree(pre[0], rebuild_from_pre_in(pre[1:cut + 1], ino[:cut]),
                      rebuild_from_pre_in(pre[cut + 1:], ino[cut + 1:]))


def rebuild_from_post_in(post, ino):
    """The tree with the given postorder and inorder walks."""
    if not post:
        return None
    cut = ino.index(post[-1])
    return BinaryTree(post[-1], rebuild_from_post_in(post[:cut], ino[:cut]),
                      rebuild_from_post_in(post[cut:-1], ino[cut + 1:]))


def shape(tree):
    """A string that two trees share only when they are the same tree."""
    if tree is None:
        return "."
    return f"({tree.value}{shape(tree.left)}{shape(tree.right)})"


def built(values):
    """The search tree these values give when inserted in this order."""
    t = None
    for v in values:
        t = insert(t, v)
    return t


faults = 0
print(f"{'inserted':>28} {'pre + in rebuilds':>19} {'post + in rebuilds':>20}")
for values in ([2, 1], [8, 3, 10, 1], [5, 2, 8, 1, 3, 7, 9], [8, 3, 10, 1, 6, 14, 4]):
    t = built(values)
    one = shape(rebuild_from_pre_in(preorder(t), inorder(t))) == shape(t)
    two = shape(rebuild_from_post_in(postorder(t), inorder(t))) == shape(t)
    faults += (not one) + (not two)
    print(f"{str(values):>28} {str(one):>19} {str(two):>20}")
print(f"rebuilds that did not match the original: {faults}")
print()
shapes = {}
for values in permutations([1, 2, 3]):
    shapes.setdefault(shape(built(values)), []).append(values)
print(f"the {len(shapes)} distinct trees from the six insertion orders of 1, 2, 3:")
for s, orders in sorted(shapes.items()):
    print(f"   {s}: from {[''.join(map(str, o)) for o in orders]}")

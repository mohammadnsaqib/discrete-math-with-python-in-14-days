"""One traversal does not fix a tree, and two of them do."""
from dmkit.tree import BinaryTree, inorder, insert, postorder, preorder


def rebuild(pre, ino):
    """The tree with the given preorder and inorder walks.

    The first value of the preorder is the root. Finding it in the inorder walk splits
    that walk into everything left of the root and everything right, and the preorder
    splits the same way. THAT SPLIT IS THE WHOLE ALGORITHM, and it is a structural
    induction.
    """
    if not pre:
        return None
    cut = ino.index(pre[0])
    return BinaryTree(pre[0], rebuild(pre[1:cut + 1], ino[:cut]),
                      rebuild(pre[cut + 1:], ino[cut + 1:]))


shapes = [BinaryTree(1, BinaryTree(2, None, None), None),
          BinaryTree(1, None, BinaryTree(2, None, None)),
          BinaryTree(2, BinaryTree(1, None, None), None)]
print(f"{'preorder':>12} {'inorder':>12} {'postorder':>12}")
for t in shapes:
    print(f"{str(preorder(t)):>12} {str(inorder(t)):>12} {str(postorder(t)):>12}")
print("the first two rows share a preorder and differ in their inorder")
print()
tree = None
for v in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    tree = insert(tree, v)
back = rebuild(preorder(tree), inorder(tree))
print(f"the original preorder : {preorder(tree)}")
print(f"the original inorder  : {inorder(tree)}")
print(f"the rebuilt postorder : {postorder(back)}")
print(f"the same tree: {postorder(tree) == postorder(back)}")
print()
faults = 0
for values in ([1], [1, 2], [2, 1], [8, 3, 10, 1], [5, 2, 8, 1, 3, 7, 9]):
    t = None
    for v in values:
        t = insert(t, v)
    faults += postorder(t) != postorder(rebuild(preorder(t), inorder(t)))
print(f"trees that did not rebuild from their two walks: {faults}")

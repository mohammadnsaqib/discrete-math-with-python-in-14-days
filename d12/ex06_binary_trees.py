"""A tree where each node has a left and a right, either of which may be missing."""
from dmkit.tree import BinaryTree, inorder, preorder

leaf = lambda v: BinaryTree(v)
t = BinaryTree(8,
               BinaryTree(3, leaf(1), BinaryTree(6, leaf(4), leaf(7))),
               BinaryTree(10, None, BinaryTree(14, leaf(13), None)))

print(f"size   : {t.size()}")
print(f"height : {t.height()}")
print(f"leaves : {t.leaves()}")
print(f"preorder: {preorder(t)}")
print()
shapes = [("one node", leaf(1)),
          ("a line of 3", BinaryTree(1, BinaryTree(2, leaf(3), None), None)),
          ("full of 3", BinaryTree(1, leaf(2), leaf(3))),
          ("full of 7", BinaryTree(1, BinaryTree(2, leaf(4), leaf(5)),
                                   BinaryTree(3, leaf(6), leaf(7)))),
          ("the tree above", t)]
print(f"{'shape':>18} {'size':>6} {'height':>8} {'leaves':>8} {'2**(h+1) - 1':>14} "
      f"{'size fits':>11}")
for name, tree in shapes:
    most = 2 ** (tree.height() + 1) - 1
    print(f"{name:>18} {tree.size():>6} {tree.height():>8} {len(tree.leaves()):>8} "
          f"{most:>14} {str(tree.size() <= most):>11}")

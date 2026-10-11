"""The three walks written with a stack instead of a recursion."""
from dmkit.tree import BinaryTree, inorder, insert, postorder, preorder


def preorder_by_stack(tree):
    """The node, then the left subtree, then the right, using an explicit stack."""
    out, stack = [], [tree]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        out.append(node.value)
        stack.append(node.right)
        stack.append(node.left)
    return out


def inorder_by_stack(tree):
    """The left subtree, then the node, then the right, using an explicit stack."""
    out, stack, node = [], [], tree
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        out.append(node.value)
        node = node.right
    return out


def postorder_by_stack(tree):
    """The left subtree, then the right, then the node, using an explicit stack."""
    out, stack = [], [tree]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        out.append(node.value)
        stack.append(node.left)
        stack.append(node.right)
    return out[::-1]


print(f"{'values inserted':>34} {'preorder':>10} {'inorder':>9} {'postorder':>11}")
for values in ([5], [5, 3], [5, 3, 8], [8, 3, 10, 1, 6, 14, 4, 7, 13],
               [1, 2, 3, 4, 5, 6]):
    t = None
    for v in values:
        t = insert(t, v)
    print(f"{str(values):>34} {str(preorder(t) == preorder_by_stack(t)):>10} "
          f"{str(inorder(t) == inorder_by_stack(t)):>9} "
          f"{str(postorder(t) == postorder_by_stack(t)):>11}")
print()
# BUILT WITHOUT RECURSION, because `insert` recurses once per level and a tree this deep
# would exhaust the interpreter's frames before the walk was ever reached.
deep = BinaryTree(1)
tail = deep
for v in range(2, 3001):
    tail.right = BinaryTree(v)
    tail = tail.right
print("a tree of 3000 nodes inserted in order, all leaning one way")
print(f"the stack walk reaches all of them: {len(inorder_by_stack(deep)) == 3000}")
try:
    inorder(deep)
    print("the recursion also reached all of them")
except RecursionError:
    print("the recursion raised RecursionError, which Day 4 measured")

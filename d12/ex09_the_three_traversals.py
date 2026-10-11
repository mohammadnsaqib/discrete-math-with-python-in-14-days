"""Three orders to walk a tree, and what each one is for."""
from dmkit.tree import BinaryTree, inorder, insert, postorder, preorder


def evaluate_postorder(tokens):
    """The value of an expression in postorder, using a stack and no brackets."""
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b, a = stack.pop(), stack.pop()
            stack.append({"+": a + b, "-": a - b, "*": a * b}[token])
    return stack[0]


leaf = lambda v: BinaryTree(v)
t = BinaryTree("*", BinaryTree("+", leaf("2"), leaf("3")),
               BinaryTree("-", leaf("9"), leaf("4")))
numbers = None
for v in [8, 3, 10, 1, 6, 14]:
    numbers = insert(numbers, v)

print("the tree is the expression (2 + 3) * (9 - 4)")
print(f"{'order':>12} {'the values':>26} {'on a search tree':>26} {'sorted':>8}")
for name, walk in (("preorder", preorder), ("inorder", inorder),
                   ("postorder", postorder)):
    got = walk(numbers)
    print(f"{name:>12} {' '.join(walk(t)):>26} {str(got):>26} "
          f"{str(got == sorted(got)):>8}")
print()
print(f"the postorder tokens: {postorder(t)}")
print(f"evaluated with a stack: {evaluate_postorder(postorder(t))}, "
      f"and directly: {(2 + 3) * (9 - 4)}")

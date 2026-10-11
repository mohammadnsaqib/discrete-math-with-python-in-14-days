"""How many shapes a binary tree of each size can take."""
from dmkit.tree import BinaryTree


def all_shapes(n):
    """Every binary tree shape with n nodes, in a fixed order.

    The recursion is a counting argument: a tree of n nodes is a root, a left subtree of
    k nodes and a right subtree of n-1-k, for every k. That is Day 5's product rule
    inside Day 5's sum rule, and Day 8 met the same recurrence.
    """
    if n == 0:
        return [None]
    return [BinaryTree(0, left, right)
            for k in range(n)
            for left in all_shapes(k)
            for right in all_shapes(n - 1 - k)]


counts = [len(all_shapes(n)) for n in range(0, 9)]
print(f"{'nodes':>7} {'shapes':>9} {'shortest height':>17} {'tallest height':>16} "
      f"{'the next count from the last':>30} {'agree':>7}")
for n in range(1, 9):
    heights = [t.height() for t in all_shapes(n)]
    predicted = counts[n - 1] * 2 * (2 * n - 1) // (n + 1)
    print(f"{n:>7} {counts[n]:>9} {min(heights):>17} {max(heights):>16} "
          f"{predicted:>30} {str(counts[n] == predicted):>7}")

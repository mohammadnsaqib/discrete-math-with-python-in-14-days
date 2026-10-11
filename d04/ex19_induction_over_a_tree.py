"""A claim about every expression tree, proved by induction on how trees are built."""

# A TREE IS A NUMBER, OR AN OPERATOR WITH TWO TREES UNDER IT. That definition is the
# induction: the base case is a number, and the step assumes the claim for both
# subtrees.


def count_leaves(t):
    """How many numbers are at the bottom of the tree."""
    if not isinstance(t, tuple):
        return 1
    return count_leaves(t[1]) + count_leaves(t[2])


def count_operators(t):
    """How many operator nodes the tree has."""
    if not isinstance(t, tuple):
        return 0
    return 1 + count_operators(t[1]) + count_operators(t[2])


def evaluate(t):
    """The value of the tree, computed bottom upwards."""
    if not isinstance(t, tuple):
        return t
    op, left, right = t
    a, b = evaluate(left), evaluate(right)
    return a + b if op == "+" else a * b


def as_text(t):
    """The tree written with every grouping shown."""
    if not isinstance(t, tuple):
        return str(t)
    return f"({as_text(t[1])} {t[0]} {as_text(t[2])})"


def all_trees(leaves):
    """Every tree with the given numbers at its leaves, in that order, in a fixed order.
    """
    if len(leaves) == 1:
        return [leaves[0]]
    out = []
    for cut in range(1, len(leaves)):
        for left in all_trees(leaves[:cut]):
            for right in all_trees(leaves[cut:]):
                for op in ("+", "*"):
                    out.append((op, left, right))
    return out


print(f"{'tree':>26} {'leaves':>7} {'operators':>10} {'value':>7}")
for t in all_trees((2, 3, 4))[:6]:
    print(f"{as_text(t):>26} {count_leaves(t):>7} {count_operators(t):>10} "
          f"{evaluate(t):>7}")
print()
every = [t for k in range(1, 6) for t in all_trees(tuple(range(1, k + 1)))]
bad = [t for t in every if count_leaves(t) != count_operators(t) + 1]
print(f"trees built from 1 to 5 leaves: {len(every)}")
print(f"trees where leaves did not equal operators plus one: {len(bad)}")

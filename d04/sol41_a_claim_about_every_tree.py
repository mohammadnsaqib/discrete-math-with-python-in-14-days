"""Problem 4.28: two claims about every binary tree, checked over every small one."""


def leaves(t):
    """How many numbers sit at the bottom."""
    return 1 if not isinstance(t, tuple) else leaves(t[1]) + leaves(t[2])


def operators(t):
    """How many operator nodes the tree has."""
    return 0 if not isinstance(t, tuple) else 1 + operators(t[1]) + operators(t[2])


def height(t):
    """The longest route from the top to a leaf, counting edges."""
    return 0 if not isinstance(t, tuple) else 1 + max(height(t[1]), height(t[2]))


def nodes(t):
    """Every node, leaf or operator."""
    return leaves(t) + operators(t)


def all_trees(values):
    """Every binary tree over the given leaves in the given order, in a fixed order.

    The order is fixed by the loop rather than by set iteration, so two runs of this
    program print the same trees in the same sequence.
    """
    if len(values) == 1:
        return [values[0]]
    out = []
    for cut in range(1, len(values)):
        for left in all_trees(values[:cut]):
            for right in all_trees(values[cut:]):
                out.append(("op", left, right))
    return out


print(f"{'leaves':>8} {'trees':>8} {'leaves = operators + 1':>24} "
      f"{'nodes <= 2**(h+1) - 1':>24}")
for k in range(1, 8):
    built = all_trees(tuple(range(k)))
    claim_one = all(leaves(t) == operators(t) + 1 for t in built)
    claim_two = all(nodes(t) <= 2 ** (height(t) + 1) - 1 for t in built)
    print(f"{k:>8} {len(built):>8} {str(claim_one):>24} {str(claim_two):>24}")
print()
built = all_trees(tuple(range(5)))
tallest = max(built, key=height)
shortest = min(built, key=height)
print(f"of the {len(built)} trees over 5 leaves, the tallest has height "
      f"{height(tallest)}")
print(f"and the shortest has height {height(shortest)}. Both have {leaves(tallest)} "
      f"leaves")
print(f"and {operators(tallest)} operators.")
print()
print(f"{'leaves':>8} {'trees at the bound':>20}")
for k in (1, 2, 3, 4, 5, 8):
    tight = [t for t in all_trees(tuple(range(k)))
             if nodes(t) == 2 ** (height(t) + 1) - 1]
    print(f"{k:>8} {len(tight):>20}")

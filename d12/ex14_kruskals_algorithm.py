"""Taking cheap edges, and refusing the ones that close a cycle."""
from dmkit.tree import (all_spanning_trees, is_tree, kruskal, total_weight,
                        weighted_graph)

g, weights = weighted_graph([("a", "b", 4), ("a", "c", 1), ("b", "c", 2),
                             ("b", "d", 5), ("c", "d", 8), ("c", "e", 10),
                             ("d", "e", 2), ("d", "f", 6), ("e", "f", 3)])
parent = {v: v for v in g.vertices()}


def root(v):
    """The name of the piece a vertex belongs to."""
    while parent[v] != v:
        parent[v] = parent[parent[v]]
        v = parent[v]
    return v


print(f"{'edge':>10} {'weight':>8} {'joins two pieces':>18} {'taken':>7}")
for a, b in sorted(g.edges(), key=lambda e: (weights[e], e)):
    ra, rb = root(a), root(b)
    if ra != rb:
        parent[ra] = rb
    print(f"{str((a, b)):>10} {weights[(a, b)]:>8} {str(ra != rb):>18} "
          f"{str(ra != rb):>7}")
print()
tree = kruskal(g, weights)
every = all_spanning_trees(g)
best = min(sum(weights[e] for e in t) for t in every)
print(f"the tree: {tree.edges()}, a tree: {is_tree(tree)}, "
      f"total weight {total_weight(tree, weights)}")
print(f"the cheapest over all {len(every)} spanning trees: {best}, "
      f"and they agree: {total_weight(tree, weights) == best}")

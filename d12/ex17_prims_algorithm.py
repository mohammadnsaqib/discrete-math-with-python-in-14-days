"""Growing one piece outward, taking the cheapest edge that leaves it."""
from dmkit.tree import (all_spanning_trees, is_tree, prim, total_weight,
                        weighted_graph)

g, weights = weighted_graph([("a", "b", 4), ("a", "c", 1), ("b", "c", 2),
                             ("b", "d", 5), ("c", "d", 8), ("c", "e", 10),
                             ("d", "e", 2), ("d", "f", 6), ("e", "f", 3)])
vs = g.vertices()
inside = {vs[0]}
print(f"{'inside so far':>26} {'cheapest edge leaving':>24} {'weight':>8}")
while len(inside) < len(vs):
    weight, edge = min((weights[tuple(sorted((a, b)))], tuple(sorted((a, b))))
                       for a in inside for b in g.neighbours(a) if b not in inside)
    print(f"{str(sorted(inside)):>26} {str(edge):>24} {weight:>8}")
    inside.update(edge)
print()
tree = prim(g, weights)
best = min(sum(weights[e] for e in t) for t in all_spanning_trees(g))
print(f"the tree: {tree.edges()}, a tree: {is_tree(tree)}, "
      f"total weight {total_weight(tree, weights)}")
print(f"the cheapest possible: {best}, and they agree: "
      f"{total_weight(tree, weights) == best}")
print()
print(f"{'starting vertex':>18} {'the tree':>26} {'weight':>8}")
for start in vs:
    t = prim(g, weights, start)
    print(f"{start:>18} {' '.join(a + b for a, b in t.edges()):>26} "
          f"{total_weight(t, weights):>8}")

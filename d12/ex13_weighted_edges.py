"""Edges that carry a cost, and what that changes."""
from dmkit.tree import all_spanning_trees, total_weight, weighted_graph
from dmkit.graph import Graph

g, weights = weighted_graph([("a", "b", 4), ("a", "c", 1), ("b", "c", 2),
                             ("b", "d", 5), ("c", "d", 8), ("c", "e", 10),
                             ("d", "e", 2), ("d", "f", 6), ("e", "f", 3)])
print(f"{'edge':>10} {'weight':>8}")
for edge in g.edges():
    print(f"{str(edge):>10} {weights[edge]:>8}")
print()
trees = all_spanning_trees(g)
costs = sorted((sum(weights[e] for e in tree), tree) for tree in trees)
print(f"spanning trees: {len(trees)}")
print(f"the cheapest costs {costs[0][0]}: {costs[0][1]}")
print(f"the dearest costs {costs[-1][0]}: {costs[-1][1]}")
print()
print(f"{'total weight':>14} {'trees with it':>15}")
tally = {}
for cost, _ in costs:
    tally[cost] = tally.get(cost, 0) + 1
for cost in sorted(tally)[:8]:
    print(f"{cost:>14} {tally[cost]:>15}")
print(f"{'...':>14} {f'{len(trees)} in all':>15}")
print()
print("Every spanning tree has the same number of edges and they do not cost the same.")
print(f"The cheapest is {costs[0][0]} and the dearest is {costs[-1][0]}, over "
      f"{len(trees)} trees.")
print("Finding the cheapest one without listing the rest is what Kruskal and Prim do.")

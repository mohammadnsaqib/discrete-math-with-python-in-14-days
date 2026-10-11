"""One weighted graph taken through every routine of the chapter."""
import networkx as nx

from dmkit.graph import shortest_path
from dmkit.tree import (all_spanning_trees, dijkstra, is_tree, kruskal, prim,
                        route_from, spanning_tree, total_weight, weighted_graph)

g, weights = weighted_graph([("a", "b", 7), ("a", "c", 9), ("a", "f", 14),
                             ("b", "c", 10), ("b", "d", 15), ("c", "d", 11),
                             ("c", "f", 2), ("d", "e", 6), ("e", "f", 9)])
other = nx.Graph()
other.add_nodes_from(g.vertices())
for a, b in g.edges():
    other.add_edge(a, b, weight=weights[(a, b)])
plain, by_k, by_p = spanning_tree(g), kruskal(g, weights), prim(g, weights)
cheapest = min(sum(weights[e] for e in t) for t in all_spanning_trees(g))
theirs = nx.minimum_spanning_tree(other)

print("the graph: " + "  ".join(f"{a}{b}:{weights[(a, b)]}" for a, b in g.edges()))
print(f"{'tree':>24} {'edges':>7} {'a tree':>8} {'weight':>8}")
for name, t in (("from a traversal", plain), ("by Kruskal", by_k), ("by Prim", by_p)):
    print(f"{name:>24} {len(t.edges()):>7} {str(is_tree(t)):>8} "
          f"{total_weight(t, weights):>8}")
print(f"{'the cheapest possible':>24} {'-':>7} {'-':>8} {cheapest:>8}")
print(f"{'NetworkX':>24} {theirs.number_of_edges():>7} {'-':>8} "
      f"{sum(d['weight'] for _, _, d in theirs.edges(data=True)):>8}")
print(f"Kruskal's tree: {' '.join(a + b for a, b in by_k.edges())}, "
      f"Prim's: {' '.join(a + b for a, b in by_p.edges())}")
print()
result = dijkstra(g, weights, "a")
print(f"{'to':>5} {'by cost':>10} {'cost':>7} {'by steps':>10} {'its cost':>10} "
      f"{'NetworkX cost':>15}")
for end in g.vertices():
    steps = shortest_path(g, "a", end)
    print(f"{end:>5} {''.join(route_from(result['parent'], end)):>10} "
          f"{result['cost'][end]:>7} {''.join(steps):>10} "
          f"{sum(weights[tuple(sorted(p))] for p in zip(steps, steps[1:])):>10} "
          f"{nx.dijkstra_path_length(other, 'a', end):>15}")

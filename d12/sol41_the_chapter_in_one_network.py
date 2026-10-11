"""Problem 12.28: one weighted graph through every routine the chapter built."""
import networkx as nx

from dmkit.graph import shortest_path
from dmkit.tree import (all_spanning_trees, dijkstra, is_tree, kruskal, prim,
                        route_from, spanning_tree, total_weight, weighted_graph)

g, weights = weighted_graph([("a", "b", 2), ("a", "c", 6), ("b", "d", 5),
                             ("b", "e", 8), ("c", "d", 8), ("c", "f", 4),
                             ("d", "e", 3), ("d", "f", 7), ("e", "g", 4),
                             ("f", "g", 9)])
other = nx.Graph()
other.add_nodes_from(g.vertices())
for a, b in g.edges():
    other.add_edge(a, b, weight=weights[(a, b)])
costs = [sum(weights[e] for e in t) for t in all_spanning_trees(g)]
by_k, by_p, plain = kruskal(g, weights), prim(g, weights), spanning_tree(g)
theirs = nx.minimum_spanning_tree(other)

print(f"{len(g.vertices())} vertices, {len(g.edges())} edges, "
      f"{len(costs)} spanning trees")
print(f"{'route to the tree':>26} {'edges':>7} {'a tree':>8} {'weight':>8}")
for name, t in (("a traversal", plain), ("Kruskal", by_k), ("Prim", by_p)):
    print(f"{name:>26} {len(t.edges()):>7} {str(is_tree(t)):>8} "
          f"{total_weight(t, weights):>8}")
print(f"{'NetworkX':>26} {theirs.number_of_edges():>7} {'-':>8} "
      f"{sum(d['weight'] for _, _, d in theirs.edges(data=True)):>8}")
print(f"{'the cheapest of all':>26} {'-':>7} {'-':>8} {min(costs):>8}")
print(f"{'the dearest of all':>26} {'-':>7} {'-':>8} {max(costs):>8}")
print(f"Kruskal and Prim give the same tree: {by_k.edges() == by_p.edges()}")
print()
result = dijkstra(g, weights, "a")
print(f"{'to':>5} {'cheapest':>12} {'cost':>7} {'fewest steps':>14} {'its cost':>10}")
for end in g.vertices():
    steps = shortest_path(g, "a", end)
    print(f"{end:>5} {''.join(route_from(result['parent'], end)):>12} "
          f"{result['cost'][end]:>7} {''.join(steps):>14} "
          f"{sum(weights[tuple(sorted(p))] for p in zip(steps, steps[1:])):>10}")
disagreed = sum(1 for e in g.vertices()
                if result['cost'][e] != nx.dijkstra_path_length(other, 'a', e))
print(f"costs that disagreed with NetworkX: {disagreed}")

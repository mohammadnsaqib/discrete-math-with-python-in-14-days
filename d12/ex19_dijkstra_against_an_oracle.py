"""Cheapest routes, against a library's answer for the same graph."""
import networkx as nx

from dmkit.tree import dijkstra, route_from, weighted_graph


def as_networkx(graph, weights):
    """The same weighted graph, handed to NetworkX."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    for a, b in graph.edges():
        other.add_edge(a, b, weight=weights[(a, b)])
    return other


cases = [
    ("six vertices", [("a", "b", 4), ("a", "c", 1), ("b", "c", 2), ("b", "d", 5),
                      ("c", "d", 8), ("c", "e", 10), ("d", "e", 2), ("d", "f", 6),
                      ("e", "f", 3)]),
    ("a weighted ring", [("a", "b", 1), ("b", "c", 2), ("c", "d", 3), ("d", "a", 4)]),
    ("one heavy edge", [("a", "b", 1), ("b", "c", 1), ("c", "d", 1), ("a", "d", 10)]),
    ("a grid", [("a", "b", 3), ("b", "c", 1), ("a", "d", 2), ("b", "e", 4),
                ("c", "f", 5), ("d", "e", 1), ("e", "f", 2)]),
]
print(f"{'graph':>18} {'vertices':>10} {'costs match':>13} {'the dearest route':>19}")
for name, triples in cases:
    g, weights = weighted_graph(triples)
    start = g.vertices()[0]
    mine = dijkstra(g, weights, start)["cost"]
    theirs = nx.single_source_dijkstra_path_length(as_networkx(g, weights), start)
    print(f"{name:>18} {len(g.vertices()):>10} "
          f"{str(mine == dict(theirs)):>13} {max(mine.values()):>19}")
print()
g, weights = weighted_graph(cases[0][1])
result = dijkstra(g, weights, "a")
other = as_networkx(g, weights)
print(f"{'to':>5} {'cost':>7} {'NetworkX cost':>15} {'route':>10} "
      f"{'NetworkX route':>16}")
for end in g.vertices():
    mine = route_from(result["parent"], end)
    theirs = nx.dijkstra_path(other, "a", end)
    print(f"{end:>5} {result['cost'][end]:>7} "
          f"{nx.dijkstra_path_length(other, 'a', end):>15} {''.join(mine):>10} "
          f"{''.join(theirs):>16}")

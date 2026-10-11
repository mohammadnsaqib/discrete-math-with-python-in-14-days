"""The book's minimum spanning tree against one built by a library."""
import networkx as nx

from dmkit.tree import kruskal, total_weight, weighted_graph


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
    ("a weighted line", [("a", "b", 7), ("b", "c", 2), ("c", "d", 9)]),
    ("all weights equal", [("a", "b", 1), ("b", "c", 1), ("c", "a", 1),
                           ("c", "d", 1), ("d", "a", 1)]),
    ("one heavy edge", [("a", "b", 1), ("b", "c", 1), ("c", "d", 1), ("d", "a", 100)]),
]
print(f"{'graph':>20} {'edges':>7} {'tree edges':>12} {'the book':>10} "
      f"{'NetworkX':>10} {'agree':>7}")
for name, triples in cases:
    g, weights = weighted_graph(triples)
    tree = kruskal(g, weights)
    theirs = nx.minimum_spanning_tree(as_networkx(g, weights))
    their_weight = sum(d["weight"] for _, _, d in theirs.edges(data=True))
    print(f"{name:>20} {len(g.edges()):>7} {len(tree.edges()):>12} "
          f"{total_weight(tree, weights):>10} {their_weight:>10} "
          f"{str(total_weight(tree, weights) == their_weight):>7}")
print()
g, weights = weighted_graph(cases[0][1])
tree = kruskal(g, weights)
theirs = nx.minimum_spanning_tree(as_networkx(g, weights))
their_edges = sorted(tuple(sorted(e)) for e in theirs.edges())
print(f"the book's tree: {tree.edges()}")
print(f"NetworkX's tree: {their_edges}")
print(f"the same edges : {tree.edges() == their_edges}")

"""A tree touching every vertex of a graph."""
import networkx as nx

from dmkit.graph import Graph, complete_graph, cycle_graph, path_graph
from dmkit.tree import is_tree, spanning_tree


def as_networkx(graph):
    """The same graph, handed to NetworkX."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    return other


cases = [("a ring of 6", cycle_graph(6)), ("complete on 5", complete_graph(5)),
         ("a line of 6", path_graph(6)),
         ("two triangles joined", Graph(range(6), [(0, 1), (1, 2), (2, 0),
                                                   (3, 4), (4, 5), (5, 3), (2, 3)]))]
print(f"{'graph':>24} {'vertices':>10} {'edges':>7} {'tree edges':>12} "
      f"{'a tree':>8} {'NetworkX agrees':>17}")
for name, g in cases:
    t = spanning_tree(g)
    theirs = nx.minimum_spanning_tree(as_networkx(g))
    print(f"{name:>24} {len(g.vertices()):>10} {len(g.edges()):>7} "
          f"{len(t.edges()):>12} {str(is_tree(t)):>8} "
          f"{str(len(t.edges()) == theirs.number_of_edges()):>17}")
print()
g = cases[3][1]
t = spanning_tree(g)
print(f"the graph's edges: {g.edges()}")
print(f"the tree's edges : {t.edges()}")
print(f"the edges dropped: {sorted(set(g.edges()) - set(t.edges()))}")

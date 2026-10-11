"""Whether a graph is one piece, and what the pieces are."""
import networkx as nx

from dmkit.graph import Graph, components, cycle_graph, path_graph


def as_networkx(graph):
    """The same graph, handed to NetworkX."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    return other


cases = [("a ring of 5", cycle_graph(5)),
         ("a line of 5", path_graph(5)),
         ("five isolated", Graph(range(5))),
         ("two triangles", Graph(range(6), [(0, 1), (1, 2), (2, 0),
                                            (3, 4), (4, 5), (5, 3)])),
         ("two triangles joined", Graph(range(6), [(0, 1), (1, 2), (2, 0),
                                                   (3, 4), (4, 5), (5, 3), (2, 3)]))]
print(f"{'graph':>22} {'pieces':>8} {'NetworkX':>10} {'agree':>7} "
      f"{'largest piece':>15}")
for name, g in cases:
    mine = components(g)
    theirs = sorted(sorted(c) for c in nx.connected_components(as_networkx(g)))
    print(f"{name:>22} {len(mine):>8} {len(theirs):>10} {str(mine == theirs):>7} "
          f"{max(len(c) for c in mine):>15}")
print()
print(f"the pieces of two triangles       : {components(cases[3][1])}")
print(f"the pieces of two triangles joined: {components(cases[4][1])}")

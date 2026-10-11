"""Graphs that can be drawn with no edge crossing another."""
import networkx as nx

from dmkit.colour import complete_bipartite
from dmkit.graph import Graph, complete_graph, cycle_graph, path_graph


def as_networkx(graph):
    """The same graph, handed to NetworkX."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    return other


cases = [("a line of 6", path_graph(6)), ("a ring of 6", cycle_graph(6)),
         ("complete on 4", complete_graph(4)), ("complete on 5", complete_graph(5)),
         ("complete on 6", complete_graph(6)),
         ("complete 2 by 3", complete_bipartite(2, 3)),
         ("complete 3 by 3", complete_bipartite(3, 3)),
         ("a wheel of 5", Graph(range(6), [(i, (i + 1) % 5) for i in range(5)]
                                + [(5, i) for i in range(5)]))]
print(f"{'graph':>18} {'vertices':>10} {'edges':>7} {'3n - 6':>9} "
      f"{'under the bound':>17} {'planar':>8}")
for name, g in cases:
    n = len(g.vertices())
    bound = 3 * n - 6 if n >= 3 else n * (n - 1) // 2
    planar, _ = nx.check_planarity(as_networkx(g))
    print(f"{name:>18} {n:>10} {len(g.edges()):>7} {bound:>9} "
          f"{str(len(g.edges()) <= bound):>17} {str(planar):>8}")

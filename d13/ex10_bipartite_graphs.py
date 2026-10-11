"""Graphs whose vertices split into two groups with every edge running between them."""
import networkx as nx

from dmkit.colour import (bipartite_parts, chromatic_number, complete_bipartite,
                          is_bipartite)
from dmkit.graph import Graph, complete_graph, cycle_graph, path_graph


def as_networkx(graph):
    """The same graph, handed to NetworkX."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    return other


cases = [("a line of 5", path_graph(5)), ("a ring of 4", cycle_graph(4)),
         ("a ring of 5", cycle_graph(5)), ("complete on 3", complete_graph(3)),
         ("a star of 6", Graph(range(6), [(0, i) for i in range(1, 6)])),
         ("complete 3 by 3", complete_bipartite(3, 3)),
         ("a crown of 6", Graph("abcdef", [("a", "d"), ("b", "e"), ("c", "f"),
                                           ("a", "e"), ("b", "f"), ("c", "d")]))]
print(f"{'graph':>18} {'bipartite':>11} {'NetworkX agrees':>17} "
      f"{'the fewest colours':>20} {'group sizes':>13}")
for name, g in cases:
    mine = is_bipartite(g)
    parts = bipartite_parts(g)
    sizes = f"{len(parts[0])}, {len(parts[1])}" if parts else "-"
    print(f"{name:>18} {str(mine):>11} "
          f"{str(mine == nx.is_bipartite(as_networkx(g))):>17} "
          f"{chromatic_number(g):>20} {sizes:>13}")
print()
mismatch = [name for name, g in cases
            if is_bipartite(g) != (chromatic_number(g) <= 2)]
print(f"graphs where bipartite and two-colourable disagree: {mismatch}")

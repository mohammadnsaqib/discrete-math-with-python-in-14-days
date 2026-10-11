"""Where the edge bound comes from, counted rather than quoted."""
import networkx as nx

from dmkit.colour import complete_bipartite, edge_bound
from dmkit.graph import Graph, complete_graph, cycle_graph


def face_sizes(graph):
    """How many edges border each face of a planar drawing."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    planar, embedding = nx.check_planarity(other)
    if not planar:
        return None
    seen, sizes = set(), []
    for a, b in list(embedding.edges()):
        if (a, b) in seen:
            continue
        sizes.append(len(list(embedding.traverse_face(a, b, mark_half_edges=seen))))
    return sorted(sizes)


cases = [("a ring of 5", cycle_graph(5)), ("complete on 4", complete_graph(4)),
         ("complete 2 by 3", complete_bipartite(2, 3)),
         ("a wheel of 5", Graph(range(6), [(i, (i + 1) % 5) for i in range(5)]
                                + [(5, i) for i in range(5)]))]
print(f"{'graph':>18} {'edges':>7} {'faces':>7} {'face sizes':>22} "
      f"{'they add to':>13} {'twice the edges':>17}")
for name, g in cases:
    sizes = face_sizes(g)
    print(f"{name:>18} {len(g.edges()):>7} {len(sizes):>7} {str(sizes):>22} "
          f"{sum(sizes):>13} {2 * len(g.edges()):>17}")
print()
print(f"{'graph':>18} {'smallest face':>15} {'3 times faces':>15} "
      f"{'twice the edges':>17} {'so edges at most':>18}")
for name, g in cases:
    sizes = face_sizes(g)
    print(f"{name:>18} {min(sizes):>15} {3 * len(sizes):>15} "
          f"{2 * len(g.edges()):>17} "
          f"{edge_bound(len(g.vertices()), min(sizes)):>18}")

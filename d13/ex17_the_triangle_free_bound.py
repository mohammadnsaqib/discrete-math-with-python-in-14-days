"""A tighter bound for graphs with no triangle, and what it settles."""
from itertools import combinations

import networkx as nx

from dmkit.colour import complete_bipartite, edge_bound
from dmkit.graph import complete_graph, cycle_graph


def as_networkx(graph):
    """The same graph, handed to NetworkX."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    return other


def has_triangle(graph):
    """True when three vertices are all joined to each other."""
    return any(all(b in graph.adjacency[a] for a, b in combinations(three, 2))
               for three in combinations(graph.vertices(), 3))


cases = [("a ring of 6", cycle_graph(6)), ("complete on 4", complete_graph(4)),
         ("complete on 5", complete_graph(5)),
         ("complete 2 by 3", complete_bipartite(2, 3)),
         ("complete 3 by 3", complete_bipartite(3, 3)),
         ("complete 3 by 4", complete_bipartite(3, 4))]
print(f"{'graph':>18} {'vertices':>10} {'edges':>7} {'a triangle':>12} "
      f"{'the bound that applies':>24} {'ruled out':>11} {'planar':>8}")
for name, g in cases:
    n = len(g.vertices())
    triangle = has_triangle(g)
    bound = edge_bound(n, 3 if triangle else 4)
    planar, _ = nx.check_planarity(as_networkx(g))
    print(f"{name:>18} {n:>10} {len(g.edges()):>7} {str(triangle):>12} "
          f"{bound:>24} {str(len(g.edges()) > bound):>11} {str(planar):>8}")

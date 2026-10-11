"""What stops a graph being bipartite is exactly an odd cycle."""
from itertools import combinations

import networkx as nx

from dmkit.colour import is_bipartite
from dmkit.graph import Graph, cycle_graph


def shortest_odd_cycle(graph):
    """The length of the shortest closed path of odd length, or None."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    lengths = [len(c) for c in nx.simple_cycles(other) if len(c) % 2 == 1]
    return min(lengths) if lengths else None


cases = [("a ring of 4", cycle_graph(4)), ("a ring of 5", cycle_graph(5)),
         ("a ring of 6", cycle_graph(6)), ("a ring of 7", cycle_graph(7)),
         ("two triangles joined", Graph(range(6), [(0, 1), (1, 2), (2, 0),
                                                   (3, 4), (4, 5), (5, 3), (2, 3)])),
         ("a square with a diagonal",
          Graph(range(4), [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]))]
print(f"{'graph':>26} {'bipartite':>11} {'shortest odd cycle':>20} {'agree':>7}")
for name, g in cases:
    odd = shortest_odd_cycle(g)
    print(f"{name:>26} {str(is_bipartite(g)):>11} {str(odd):>20} "
          f"{str(is_bipartite(g) == (odd is None)):>7}")
print()
possible = list(combinations(range(5), 2))
faults = tested = 0
for k in range(len(possible) + 1):
    for chosen in combinations(possible, k):
        g = Graph(range(5), chosen)
        tested += 1
        faults += is_bipartite(g) != (shortest_odd_cycle(g) is None)
print(f"graphs on 5 vertices tested: {tested}")
print(f"graphs where bipartite and 'no odd cycle' disagreed: {faults}")

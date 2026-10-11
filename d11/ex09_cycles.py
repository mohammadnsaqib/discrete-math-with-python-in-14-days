"""A closed path, and how many a graph has."""
from itertools import combinations

import networkx as nx

from dmkit.graph import Graph, complete_graph, cycle_graph, path_graph


def as_networkx(graph):
    """The same graph, handed to NetworkX."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    return other


print(f"{'graph':>26} {'vertices':>10} {'edges':>7} {'cycles':>8} {'shortest':>10}")
for name, g in (("a ring of 5", cycle_graph(5)), ("a line of 5", path_graph(5)),
                ("complete on 4", complete_graph(4)),
                ("complete on 5", complete_graph(5)),
                ("a square with a diagonal",
                 Graph("abcd", [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a"),
                                ("a", "c")]))):
    other = as_networkx(g)
    found = list(nx.simple_cycles(other))
    shortest = min((len(c) for c in found), default=0)
    print(f"{name:>26} {len(g.vertices()):>10} "
          f"{len(g.edges()):>7} {len(found):>8} {shortest if found else '-':>10}")
print()
g = Graph("abcd", [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a"), ("a", "c")])
cycles = sorted(sorted(c) for c in nx.simple_cycles(as_networkx(g)))
print(f"the cycles of the square with a diagonal: {cycles}")
print()
print(f"{'vertices':>10} {'edges in a ring':>17} {'cycles':>8}")
for n in range(3, 8):
    other = as_networkx(cycle_graph(n))
    print(f"{n:>10} {n:>17} {len(list(nx.simple_cycles(other))):>8}")

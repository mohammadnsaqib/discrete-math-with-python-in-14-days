"""Problem 13.26: bipartite, two-colourable and odd-cycle-free, over every small graph.
"""
from itertools import combinations

import networkx as nx

from dmkit.colour import bipartite_parts, chromatic_number, is_bipartite
from dmkit.graph import Graph


def as_networkx(graph):
    """The same graph, handed to NetworkX."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    return other


def has_odd_cycle(graph):
    """True when some closed path of odd length exists."""
    return any(len(c) % 2 == 1 for c in nx.simple_cycles(as_networkx(graph)))


print(f"{'vertices':>10} {'graphs':>8} {'bipartite':>11} {'two-colourable':>16} "
      f"{'no odd cycle':>14} {'all three agree':>17}")
for n in range(2, 6):
    possible = list(combinations(range(n), 2))
    total = bip = two = odd_free = agree = 0
    for k in range(len(possible) + 1):
        for chosen in combinations(possible, k):
            g = Graph(range(n), chosen)
            total += 1
            b = is_bipartite(g)
            c = chromatic_number(g) <= 2
            o = not has_odd_cycle(g)
            bip += b
            two += c
            odd_free += o
            agree += b == c == o
    print(f"{n:>10} {total:>8} {bip:>11} {two:>16} {odd_free:>14} "
          f"{str(agree == total):>17}")
print()
print(f"{'graph':>26} {'bipartite':>11} {'the two groups':>34}")
for name, g in (("a ring of 4", Graph(range(4), [(i, (i + 1) % 4) for i in range(4)])),
                ("a ring of 5", Graph(range(5), [(i, (i + 1) % 5) for i in range(5)])),
                ("a star of 5", Graph(range(5), [(0, i) for i in range(1, 5)])),
                ("a line of 6", Graph(range(6), [(i, i + 1) for i in range(5)]))):
    parts = bipartite_parts(g)
    print(f"{name:>26} {str(is_bipartite(g)):>11} {str(parts):>34}")

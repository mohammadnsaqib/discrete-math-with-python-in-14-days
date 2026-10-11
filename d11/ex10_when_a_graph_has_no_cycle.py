"""Graphs with no cycle at all, counted over every small case."""
from itertools import combinations

import networkx as nx

from dmkit.graph import Graph

vertices = list(range(4))
possible = list(combinations(vertices, 2))
print(f"{'edges':>7} {'graphs':>8} {'with no cycle':>15} {'connected':>11} "
      f"{'both':>7}")
for k in range(len(possible) + 1):
    graphs = list(combinations(possible, k))
    acyclic = connected = both = 0
    for chosen in graphs:
        other = nx.Graph()
        other.add_nodes_from(vertices)
        other.add_edges_from(chosen)
        no_cycle = not list(nx.simple_cycles(other))
        one_piece = nx.is_connected(other)
        acyclic += no_cycle
        connected += one_piece
        both += no_cycle and one_piece
    print(f"{k:>7} {len(graphs):>8} {acyclic:>15} {connected:>11} {both:>7}")

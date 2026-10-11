"""A closed walk using every edge exactly once, decided by a theorem rather than a
search."""
import networkx as nx

from dmkit.graph import (Graph, complete_graph, cycle_graph, degrees, euler_circuit,
                         has_euler_circuit, path_graph)


def as_networkx(graph):
    """The same graph, handed to NetworkX."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    return other


cases = [("a ring of 5", cycle_graph(5)),
         ("a line of 5", path_graph(5)),
         ("complete on 4", complete_graph(4)),
         ("complete on 5", complete_graph(5)),
         ("two triangles joined", Graph(range(6), [(0, 1), (1, 2), (2, 0),
                                                   (3, 4), (4, 5), (5, 3), (2, 3)])),
         ("a bowtie", Graph(range(5), [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4),
                                       (4, 2)]))]
print(f"{'graph':>24} {'edges':>7} {'odd degrees':>13} {'one piece':>11} "
      f"{'a circuit':>11} {'NetworkX agrees':>17}")
for name, g in cases:
    odd = sum(1 for d in degrees(g).values() if d % 2 == 1)
    mine = has_euler_circuit(g)
    theirs = nx.is_eulerian(as_networkx(g))
    one_piece = nx.is_connected(as_networkx(g))
    print(f"{name:>24} {len(g.edges()):>7} {odd:>13} {str(one_piece):>11} "
          f"{str(mine):>11} {str(mine == theirs):>17}")
print()
g = cases[5][1]
circuit = euler_circuit(g)
used = [tuple(sorted(pair)) for pair in zip(circuit, circuit[1:])]
print(f"a circuit on the bowtie: {circuit}")
print(f"   edges used: {len(used)}, edges in the graph: {len(g.edges())}")
print(f"   every edge once: {sorted(used) == g.edges()}")
print(f"   it closes: {circuit[0] == circuit[-1]}")

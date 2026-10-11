"""Problem 11.27: circuits found and then verified edge by edge."""
import networkx as nx

from dmkit.graph import (Graph, complete_graph, cycle_graph, degrees, euler_circuit,
                         has_euler_circuit)


def verify(graph, circuit):
    """Whether a walk really uses every edge exactly once and closes."""
    if circuit is None:
        return False
    used = [tuple(sorted(pair)) for pair in zip(circuit, circuit[1:])]
    return (sorted(used) == graph.edges() and circuit[0] == circuit[-1]
            and all(b in graph.adjacency[a] for a, b in zip(circuit, circuit[1:])))


cases = [("a ring of 6", cycle_graph(6)),
         ("complete on 5", complete_graph(5)),
         ("complete on 7", complete_graph(7)),
         ("a bowtie", Graph(range(5), [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4),
                                       (4, 2)])),
         ("two squares joined", Graph(range(7), [(0, 1), (1, 2), (2, 3), (3, 0),
                                                 (3, 4), (4, 5), (5, 6), (6, 3)])),
         ("a line of 5", Graph(range(5), [(i, i + 1) for i in range(4)]))]
faults = 0
print(f"{'graph':>22} {'edges':>7} {'odd degrees':>13} {'has one':>9} "
      f"{'circuit length':>16} {'verified':>10}")
for name, g in cases:
    other = nx.Graph()
    other.add_nodes_from(g.vertices())
    other.add_edges_from(g.edges())
    circuit = euler_circuit(g)
    odd = sum(1 for d in degrees(g).values() if d % 2 == 1)
    if has_euler_circuit(g):
        faults += not verify(g, circuit)
    faults += has_euler_circuit(g) != (nx.is_eulerian(other)
                                       or all(d == 0 for d in degrees(g).values()))
    print(f"{name:>22} {len(g.edges()):>7} {odd:>13} {str(has_euler_circuit(g)):>9} "
          f"{len(circuit) - 1 if circuit else 0:>16} {str(verify(g, circuit)):>10}")
print()
print(f"the circuit on two squares joined: {euler_circuit(cases[4][1])}")
print(f"graphs where the test and the circuit disagreed: {faults}")

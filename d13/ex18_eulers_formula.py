"""Vertices minus edges plus faces, on every drawing that can be made."""
import networkx as nx

from dmkit.colour import euler_formula_check
from dmkit.graph import Graph, complete_graph, cycle_graph, path_graph


def as_networkx(graph):
    """The same graph, handed to NetworkX."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    return other


def faces_of(graph):
    """How many regions a planar drawing cuts the plane into, from Euler's formula."""
    return len(graph.edges()) - len(graph.vertices()) + 2


def faces_from_embedding(graph):
    """The faces counted by walking each one from NetworkX's own embedding.

    Every directed edge belongs to exactly one face. Walking from an unvisited one
    traces that whole face, and the count of walks is the count of faces. This shares no
    step with Euler's formula, which is what makes it a check on it.
    """
    planar, embedding = nx.check_planarity(as_networkx(graph))
    if not planar:
        return None
    seen, faces = set(), 0
    for a, b in list(embedding.edges()):
        if (a, b) in seen:
            continue
        faces += 1
        list(embedding.traverse_face(a, b, mark_half_edges=seen))
    return faces


cases = [("a line of 5", path_graph(5)), ("a ring of 5", cycle_graph(5)),
         ("complete on 4", complete_graph(4)),
         ("a wheel of 5", Graph(range(6), [(i, (i + 1) % 5) for i in range(5)]
                                + [(5, i) for i in range(5)])),
         ("a triangle with a tail", Graph(range(4), [(0, 1), (1, 2), (2, 0), (2, 3)]))]
print(f"{'graph':>24} {'vertices':>10} {'edges':>7} {'faces':>7} {'v - e + f':>11} "
      f"{'faces by walking':>18} {'agree':>7}")
for name, g in cases:
    v, e = len(g.vertices()), len(g.edges())
    f, walked = faces_of(g), faces_from_embedding(g)
    print(f"{name:>24} {v:>10} {e:>7} {f:>7} {v - e + f:>11} {str(walked):>18} "
          f"{str(walked == f and euler_formula_check(v, e, f)):>7}")
print()
print(f"{'ring size':>12} {'vertices':>10} {'edges':>7} {'faces':>7}")
for n in range(3, 8):
    g = cycle_graph(n)
    print(f"{n:>12} {len(g.vertices()):>10} {len(g.edges()):>7} {faces_of(g):>7}")

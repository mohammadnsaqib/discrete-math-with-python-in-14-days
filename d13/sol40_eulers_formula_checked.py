"""Problem 13.27: Euler's formula on every planar graph that fits in one run."""
from itertools import combinations

import networkx as nx

from dmkit.colour import euler_formula_check
from dmkit.graph import Graph, components


def faces_by_walking(graph):
    """The faces of a planar drawing, counted by walking each one."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    planar, embedding = nx.check_planarity(other)
    if not planar:
        return None
    seen, faces = set(), 0
    for a, b in list(embedding.edges()):
        if (a, b) in seen:
            continue
        faces += 1
        list(embedding.traverse_face(a, b, mark_half_edges=seen))
    return faces


print(f"{'vertices':>10} {'connected planar graphs':>25} {'formula holds':>15} "
      f"{'faces match the walk':>22}")
for n in range(1, 6):
    possible = list(combinations(range(n), 2))
    tested = holds = matched = 0
    for k in range(len(possible) + 1):
        for chosen in combinations(possible, k):
            g = Graph(range(n), chosen)
            if len(components(g)) != 1:
                continue
            walked = faces_by_walking(g)
            if walked is None:
                continue
            tested += 1
            v, e = len(g.vertices()), len(g.edges())
            holds += euler_formula_check(v, e, e - v + 2)
            matched += walked == e - v + 2
    print(f"{n:>10} {tested:>25} {holds:>15} {matched:>22}")
print()
print(f"{'graph':>26} {'v':>4} {'e':>4} {'f':>4} {'v - e + f':>11}")
for name, g in (("a line of 5", Graph(range(5), [(i, i + 1) for i in range(4)])),
                ("a ring of 5", Graph(range(5), [(i, (i + 1) % 5) for i in range(5)])),
                ("complete on 4", Graph(range(4), list(combinations(range(4), 2)))),
                ("two triangles joined",
                 Graph(range(6), [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3),
                                  (2, 3)]))):
    v, e = len(g.vertices()), len(g.edges())
    f = faces_by_walking(g)
    print(f"{name:>26} {v:>4} {e:>4} {f:>4} {v - e + f:>11}")

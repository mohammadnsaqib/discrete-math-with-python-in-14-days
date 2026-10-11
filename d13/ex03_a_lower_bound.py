"""A set of mutually joined vertices forces that many colours."""
from itertools import combinations

from dmkit.colour import chromatic_number
from dmkit.graph import Graph, complete_graph, cycle_graph


def largest_clique(graph):
    """The largest set of vertices every two of which are joined, found by search."""
    vs = graph.vertices()
    for size in range(len(vs), 0, -1):
        for chosen in combinations(vs, size):
            if all(b in graph.adjacency[a] for a, b in combinations(chosen, 2)):
                return list(chosen)
    return []


cases = [("a ring of 5", cycle_graph(5)), ("a ring of 6", cycle_graph(6)),
         ("complete on 4", complete_graph(4)),
         ("a triangle with a tail", Graph(range(4), [(0, 1), (1, 2), (2, 0), (2, 3)])),
         ("two triangles joined", Graph(range(6), [(0, 1), (1, 2), (2, 0),
                                                   (3, 4), (4, 5), (5, 3), (2, 3)])),
         ("a five-vertex wheel", Graph(range(5), [(0, i) for i in range(1, 5)]
                                       + [(1, 2), (2, 3), (3, 4), (4, 1)]))]
print(f"{'graph':>24} {'largest clique':>16} {'that many':>11} "
      f"{'largest degree':>16} {'that plus one':>15} {'the fewest':>12}")
for name, g in cases:
    clique = largest_clique(g)
    biggest = max(len(g.adjacency[v]) for v in g.vertices())
    print(f"{name:>24} {str(clique):>16} {len(clique):>11} {biggest:>16} "
          f"{biggest + 1:>15} {chromatic_number(g):>12}")

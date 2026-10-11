"""A graph is a set of vertices and a set of edges, and nothing else."""
from dmkit.graph import Graph, complete_graph, cycle_graph, path_graph

g = Graph("abcde", [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a"), ("a", "c")])
print(f"vertices: {g.vertices()}")
print(f"edges   : {g.edges()}")
print(f"the graph: {g}")
print()
print(f"{'vertex':>8} {'neighbours':>22}")
for v in g.vertices():
    print(f"{v:>8} {str(g.neighbours(v)):>22}")
print()
print(f"{'graph':>18} {'vertices':>10} {'edges':>8} {'a sample edge':>16}")
for name, built in (("complete on 5", complete_graph(5)),
                    ("a ring of 5", cycle_graph(5)),
                    ("a line of 5", path_graph(5)),
                    ("five isolated", Graph(range(5)))):
    edges = built.edges()
    print(f"{name:>18} {len(built.vertices()):>10} {len(edges):>8} "
          f"{str(edges[0]) if edges else '-':>16}")

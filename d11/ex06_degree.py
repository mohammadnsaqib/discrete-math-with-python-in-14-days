"""How many edges meet each vertex."""
import networkx as nx

from dmkit.graph import Graph, complete_graph, cycle_graph, degrees, path_graph

g = Graph("abcde", [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a"), ("a", "c")])
d = degrees(g)
print(f"{'vertex':>8} {'degree':>8} {'neighbours':>22}")
for v in g.vertices():
    print(f"{v:>8} {d[v]:>8} {str(g.neighbours(v)):>22}")
print()
print(f"the degrees add to {sum(d.values())}, and there are {len(g.edges())} edges")
print()
print(f"{'graph':>18} {'vertices':>10} {'edges':>7} {'degrees add to':>16} "
      f"{'NetworkX agrees':>17}")
for name, built in (("complete on "
                     "5", complete_graph(5)), ("a ring of 6", cycle_graph(6)),
                    ("a line of 6", path_graph(6)), ("five isolated", Graph(range(5)))):
    other = nx.Graph()
    other.add_nodes_from(built.vertices())
    other.add_edges_from(built.edges())
    total = sum(degrees(built).values())
    same = all(degrees(built)[v] == other.degree(v) for v in built.vertices())
    print(f"{name:>18} {len(built.vertices()):>10} {len(built.edges()):>7} "
          f"{total:>16} {str(same):>17}")

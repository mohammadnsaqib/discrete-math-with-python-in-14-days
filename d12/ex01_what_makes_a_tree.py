"""A tree is connected and has no cycle, and the edge count follows."""
import networkx as nx

from dmkit.graph import Graph, complete_graph, components, cycle_graph, path_graph
from dmkit.tree import has_cycle, is_tree

cases = [("a line of 5", path_graph(5)),
         ("a ring of 5", cycle_graph(5)),
         ("a star of 5", Graph(range(5), [(0, i) for i in range(1, 5)])),
         ("complete on 4", complete_graph(4)),
         ("a triangle and a lone vertex", Graph(range(4), [(0, 1), (1, 2), (2, 0)])),
         ("two lines", Graph(range(6), [(0, 1), (1, 2), (3, 4), (4, 5)])),
         ("one vertex", Graph(range(1)))]
print(f"{'graph':>30} {'vertices':>10} {'edges':>7} {'one piece':>11} {'no cycle':>10} "
      f"{'a tree':>8} {'edges = n - 1':>15} {'NetworkX agrees':>17}")
for name, g in cases:
    other = nx.Graph()
    other.add_nodes_from(g.vertices())
    other.add_edges_from(g.edges())
    v, e = len(g.vertices()), len(g.edges())
    print(f"{name:>30} {v:>10} {e:>7} {str(len(components(g)) == 1):>11} "
          f"{str(not has_cycle(g)):>10} {str(is_tree(g)):>8} {str(e == v - 1):>15} "
          f"{str(is_tree(g) == nx.is_tree(other)):>17}")

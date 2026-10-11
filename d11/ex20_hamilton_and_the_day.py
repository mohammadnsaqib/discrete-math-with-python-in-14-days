"""A route visiting every vertex once, and why it is a different kind of question."""
import networkx as nx

from dmkit.graph import (Graph, complete_graph, cycle_graph, degrees, hamilton_path,
                         has_euler_circuit, path_graph)
from dmkit.induct import best_of

cases = [("a ring of 6", cycle_graph(6)),
         ("a line of 6", path_graph(6)),
         ("complete on 5", complete_graph(5)),
         ("a star of 5", Graph(range(5), [(0, i) for i in range(1, 5)])),
         ("two triangles joined", Graph(range(6), [(0, 1), (1, 2), (2, 0),
                                                   (3, 4), (4, 5), (5, 3), (2, 3)]))]
print(f"{'graph':>24} {'vertices':>10} {'edges':>7} {'Euler circuit':>15} "
      f"{'Hamilton path':>15}")
for name, g in cases:
    route = hamilton_path(g)
    print(f"{name:>24} {len(g.vertices()):>10} {len(g.edges()):>7} "
          f"{str(has_euler_circuit(g)):>15} "
          f"{str(route is not None):>15}")
print()
for name, g in cases:
    route = hamilton_path(g)
    print(f"{name:>24}: {route}")
print()
# THE WORST CASE IS A GRAPH WITH NO HAMILTON PATH, because then every order has to be
# tried. A complete graph finds one on the first order and says nothing about the cost.
print(f"{'star size':>11} {'orders to try':>16} {'a path exists':>15} {'seconds':>12}")
for n in (5, 6, 7, 8, 9):
    g = Graph(range(n), [(0, i) for i in range(1, n)])
    orders = 1
    for k in range(2, n + 1):
        orders *= k
    seconds = best_of(lambda x=g: hamilton_path(x), 3)
    print(f"{n:>11} {orders:>16} {str(hamilton_path(g) is not None):>15} "
          f"{seconds:>12.6f}")

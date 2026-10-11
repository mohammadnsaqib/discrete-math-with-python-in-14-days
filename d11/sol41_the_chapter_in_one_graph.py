"""Problem 11.28: one graph taken through every routine of the chapter."""
import networkx as nx

from dmkit.graph import (Graph, adjacency_matrix, bfs, components, degrees, dfs,
                         euler_circuit, hamilton_path, has_euler_circuit,
                         matrix_power, shortest_path)

g = Graph("abcdefgh", [("a", "b"), ("a", "c"), ("b", "c"), ("b", "d"), ("c", "e"),
                       ("d", "e"), ("d", "f"), ("e", "g"), ("f", "g"), ("g", "h")])
other = nx.Graph()
other.add_nodes_from(g.vertices())
other.add_edges_from(g.edges())

print(f"{'question':>34} {'the book':>22} {'NetworkX agrees':>17}")
print(f"{'vertices':>34} {len(g.vertices()):>22} "
      f"{str(len(g.vertices()) == other.number_of_nodes()):>17}")
print(f"{'edges':>34} {len(g.edges()):>22} "
      f"{str(len(g.edges()) == other.number_of_edges()):>17}")
print(f"{'pieces':>34} {len(components(g)):>22} "
      f"{str(len(components(g)) == nx.number_connected_components(other)):>17}")
d = degrees(g)
print(f"{'degrees add to':>34} {sum(d.values()):>22} "
      f"{str(sum(d.values()) == 2 * len(g.edges())):>17}")
print(f"{'largest degree':>34} {max(d.values()):>22} "
      f"{str(max(d.values()) == max(dict(other.degree()).values())):>17}")
print(f"{'an Euler circuit':>34} {str(has_euler_circuit(g)):>22} "
      f"{str(has_euler_circuit(g) == nx.is_eulerian(other)):>17}")
route = hamilton_path(g)
print(f"{'a Hamilton path':>34} {str(route is not None):>22} {'-':>17}")
print()
print(f"the degrees: {d}")
odd = [v for v in g.vertices() if d[v] % 2 == 1]
print(f"the vertices of odd degree: {odd}, and there are {len(odd)} of them")
print(f"the Hamilton path: {route}")
print()
wide = bfs(g, "a")
print(f"breadth-first from a : {wide['order']}")
print(f"the distances        : {wide['distance']}")
print(f"NetworkX agrees      : "
      f"{wide['distance'] == dict(nx.single_source_shortest_path_length(other, 'a'))}")
print(f"depth-first from a   : {dfs(g, 'a')['order']}")
print()
print(f"the route from a to h: {shortest_path(g, 'a', 'h')}")
print(f"its length           : {len(shortest_path(g, 'a', 'h')) - 1}")
agree = (len(shortest_path(g, 'a', 'h')) - 1
         == nx.shortest_path_length(other, 'a', 'h'))
print(f"NetworkX agrees      : {agree}")
print()
matrix = adjacency_matrix(g)
vs = g.vertices()
print(f"{'length':>8} {'walks from a to h':>20} {'from a to a':>14}")
for length in range(1, 6):
    powered = matrix_power(matrix, length)
    print(f"{length:>8} {powered[vs.index('a')][vs.index('h')]:>20} "
          f"{powered[vs.index('a')][vs.index('a')]:>14}")

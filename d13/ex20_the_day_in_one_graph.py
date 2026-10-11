"""One graph taken through every question the chapter asks."""
import networkx as nx

from dmkit.colour import (chromatic_number, edge_bound, euler_formula_check,
                          greedy_colour, greedy_matching, is_bipartite, is_proper,
                          maximum_matching)
from dmkit.graph import Graph, degrees

g = Graph("abcdefg", [("a", "b"), ("a", "c"), ("b", "c"), ("b", "d"), ("c", "e"),
                      ("d", "e"), ("d", "f"), ("e", "g"), ("f", "g")])
other = nx.Graph()
other.add_nodes_from(g.vertices())
other.add_edges_from(g.edges())
greedy = greedy_colour(g)
matching = maximum_matching(g)
theirs = len(set(nx.greedy_color(other).values()))
their_matching = nx.max_weight_matching(other, maxcardinality=True)
planar, _ = nx.check_planarity(other)
v, e = len(g.vertices()), len(g.edges())
faces = e - v + 2

print(f"{v} vertices, {e} edges, the degrees {degrees(g)}")
print()
print(f"{'question':>30} {'the book':>12} {'NetworkX':>12} {'agree':>7}")
print(f"{'greedy colours':>30} {len(set(greedy.values())):>12} {theirs:>12} "
      f"{str(len(set(greedy.values())) == theirs):>7}")
print(f"{'the fewest colours':>30} {chromatic_number(g):>12} {'-':>12} {'-':>7}")
print(f"{'the colouring is proper':>30} {str(is_proper(g, greedy)):>12} "
      f"{'-':>12} {'-':>7}")
print(f"{'bipartite':>30} {str(is_bipartite(g)):>12} "
      f"{str(nx.is_bipartite(other)):>12} "
      f"{str(is_bipartite(g) == nx.is_bipartite(other)):>7}")
print(f"{'largest matching':>30} {len(matching):>12} {len(their_matching):>12} "
      f"{str(len(matching) == len(their_matching)):>7}")
print(f"{'greedy matching':>30} {len(greedy_matching(g)):>12} {'-':>12} {'-':>7}")
print(f"{'planar':>30} {'-':>12} {str(planar):>12} {'-':>7}")
print()
print(f"the greedy colouring: {greedy}")
print(f"the largest matching: {matching}")
print(f"faces {faces}, v - e + f = {v - e + faces}, Euler holds: "
      f"{euler_formula_check(v, e, faces)}, and {e} edges is within {edge_bound(v)}")

"""Colouring by taking each vertex in turn and using the smallest colour left."""
import networkx as nx

from dmkit.colour import chromatic_number, greedy_colour, is_proper
from dmkit.graph import Graph, complete_graph, cycle_graph, path_graph


def as_networkx(graph):
    """The same graph, handed to NetworkX."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    return other


g = Graph("abcdef", [("a", "b"), ("a", "c"), ("b", "c"), ("b", "d"), ("c", "e"),
                     ("d", "e"), ("d", "f"), ("e", "f")])
print(f"{'vertex':>8} {'neighbours already coloured':>30} {'colours taken':>16} "
      f"{'smallest free':>15}")
seen = {}
for v in g.vertices():
    coloured = [n for n in g.neighbours(v) if n in seen]
    taken = sorted({seen[n] for n in coloured})
    c = 0
    while c in taken:
        c += 1
    seen[v] = c
    print(f"{v:>8} {str(coloured):>30} {str(taken):>16} {c:>15}")
print()
print(f"proper: {is_proper(g, seen)}, colours used: {len(set(seen.values()))}, "
      f"the fewest: {chromatic_number(g)}")
print()
print(f"{'graph':>18} {'greedy':>8} {'NetworkX greedy':>17} {'the fewest':>12}")
for name, built in (("complete on "
                     "4", complete_graph(4)), ("a ring of 5", cycle_graph(5)),
                    ("a line of 6", path_graph(6)), ("the graph above", g)):
    mine = len(set(greedy_colour(built).values()))
    theirs = len(set(nx.greedy_color(as_networkx(built)).values()))
    print(f"{name:>18} {mine:>8} {theirs:>17} {chromatic_number(built):>12}")

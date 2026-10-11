"""The greedy answer depends entirely on the order the vertices are taken."""
from itertools import permutations

from dmkit.colour import chromatic_number, greedy_colour, is_proper
from dmkit.graph import Graph

g = Graph("abcdef", [("a", "d"), ("b", "e"), ("c", "f"), ("a", "e"), ("b", "f"),
                     ("c", "d")])
print(f"the graph: {g.edges()}")
print(f"the fewest colours: {chromatic_number(g)}")
print()
worst = max(permutations(g.vertices()),
            key=lambda o: len(set(greedy_colour(g, o).values())))
print(f"{'order':>10} {'colours used':>14} {'proper':>8} "
      f"{'the colours, a to f':>22}")
for order in ["abcdef", "adbecf", "fedcba", "".join(worst)]:
    colour = greedy_colour(g, list(order))
    shown = " ".join(str(colour[v]) for v in g.vertices())
    print(f"{order:>10} {len(set(colour.values())):>14} "
          f"{str(is_proper(g, colour)):>8} {shown:>22}")
print()
counts = {}
for order in permutations(g.vertices()):
    used = len(set(greedy_colour(g, order).values()))
    counts[used] = counts.get(used, 0) + 1
total = sum(counts.values())
print(f"{'colours used':>14} {'orders giving it':>18} {'share':>8}")
for used in sorted(counts):
    print(f"{used:>14} {counts[used]:>18} {counts[used] / total:>8.4f}")

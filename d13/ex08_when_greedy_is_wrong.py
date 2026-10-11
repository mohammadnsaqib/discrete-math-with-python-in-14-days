"""A graph where every fast rule uses more colours than the graph needs."""
from itertools import permutations

from dmkit.colour import chromatic_number, greedy_colour
from dmkit.graph import Graph, degrees

# THE CROWN GRAPH. Six vertices in two groups of three, with each vertex joined to the
# two opposite it. Two colours suffice -- one per group -- and a greedy walk can be led
# astray.
g = Graph("abcdef", [("a", "d"), ("b", "e"), ("c", "f"), ("a", "e"), ("b", "f"),
                     ("c", "d")])
print(f"the degrees: {degrees(g)}")
print(f"the fewest colours: {chromatic_number(g)}")
print()
worst = max(permutations(g.vertices()),
            key=lambda o: len(set(greedy_colour(g, o).values())))
best = min(permutations(g.vertices()),
           key=lambda o: len(set(greedy_colour(g, o).values())))
for label, order in (("a good order", best), ("a bad order", worst)):
    colour = greedy_colour(g, order)
    print(f"{label:>14}: {''.join(order)} gives {len(set(colour.values()))} colours")
    print(f"{'':>14}  {{" + ", ".join(f"{v}: {colour[v]}" for v in g.vertices()) + "}")
print()
astray = sum(1 for o in permutations(g.vertices())
             if len(set(greedy_colour(g, o).values())) > chromatic_number(g))
print(f"orders of the six vertices: 720, of which {astray} are led astray")

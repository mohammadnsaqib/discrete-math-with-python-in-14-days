"""Giving each vertex a colour so that no edge has one colour at both ends."""
from dmkit.colour import greedy_colour, is_proper
from dmkit.graph import Graph

g = Graph("abcde", [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a"), ("a", "c")])
colour = greedy_colour(g)
print(f"{'vertex':>8} {'colour':>8} {'neighbours':>22} {'their colours':>16}")
for v in g.vertices():
    print(f"{v:>8} {colour[v]:>8} {str(g.neighbours(v)):>22} "
          f"{str([colour[n] for n in g.neighbours(v)]):>16}")
print()
print(f"a proper colouring: {is_proper(g, colour)}, "
      f"colours used: {len(set(colour.values()))}")
print()
bad = {"a": 0, "b": 0, "c": 1, "d": 1, "e": 0}
clashes = [(a, b) for a, b in g.edges() if bad[a] == bad[b]]
print(f"a colouring that is not proper: {bad}")
print(f"   edges with one colour at both ends: {clashes}")
print(f"   proper: {is_proper(g, bad)}")

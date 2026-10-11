"""The fewest colours a graph can be coloured with, found by searching."""
from dmkit.colour import chromatic_number, greedy_colour
from dmkit.graph import Graph, complete_graph, cycle_graph, path_graph

cases = [("a line of 5", path_graph(5)), ("a ring of 4", cycle_graph(4)),
         ("a ring of 5", cycle_graph(5)), ("complete on 4", complete_graph(4)),
         ("a star of 5", Graph(range(5), [(0, i) for i in range(1, 5)])),
         ("five isolated", Graph(range(5))),
         ("a triangle with a tail", Graph(range(4), [(0, 1), (1, 2), (2, 0), (2, 3)]))]
print(f"{'graph':>24} {'vertices':>10} {'edges':>7} {'the fewest':>12} "
      f"{'greedy uses':>13} {'greedy is best':>16}")
for name, g in cases:
    k = chromatic_number(g)
    used = len(set(greedy_colour(g).values()))
    print(f"{name:>24} {len(g.vertices()):>10} {len(g.edges()):>7} {k:>12} "
          f"{used:>13} {str(used == k):>16}")
print()
print(f"{'ring size':>12} {'the fewest colours':>20} {'odd':>6}")
for n in range(3, 9):
    print(f"{n:>12} {chromatic_number(cycle_graph(n)):>20} {str(n % 2 == 1):>6}")

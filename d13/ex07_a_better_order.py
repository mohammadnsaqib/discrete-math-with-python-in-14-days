"""Taking the busiest vertices first, measured over every graph rather than sampled."""
from itertools import combinations

from dmkit.colour import chromatic_number, greedy_colour
from dmkit.graph import Graph, complete_graph, cycle_graph, degrees


def by_degree(graph):
    """The vertices with the busiest first, ties broken by name."""
    d = degrees(graph)
    return sorted(graph.vertices(), key=lambda v: (-d[v], v))


cases = [("a ring of 5", cycle_graph(5)),
         ("complete on 4", complete_graph(4)),
         ("a crown of 6", Graph("abcdef", [("a", "d"), ("b", "e"), ("c", "f"),
                                           ("a", "e"), ("b", "f"), ("c", "d")])),
         ("a wheel of 5", Graph(range(6), [(i, (i + 1) % 5) for i in range(5)]
                                + [(5, i) for i in range(5)])),
         ("a star of 6", Graph(range(6), [(0, i) for i in range(1, 6)]))]
print(f"{'graph':>18} {'name order':>12} {'busiest first':>15} {'the fewest':>12}")
for name, g in cases:
    plain = len(set(greedy_colour(g).values()))
    busy = len(set(greedy_colour(g, by_degree(g)).values()))
    print(f"{name:>18} {plain:>12} {busy:>15} {chromatic_number(g):>12}")
print()
print("five hand-picked graphs say nothing about "
      "a rule. Every graph on five vertices does.")
print()
possible = list(combinations(range(5), 2))
tested = plain_high = busy_high = both = neither = 0
for k in range(len(possible) + 1):
    for chosen in combinations(possible, k):
        g = Graph(range(5), chosen)
        truth = chromatic_number(g)
        plain = len(set(greedy_colour(g).values())) > truth
        busy = len(set(greedy_colour(g, by_degree(g)).values())) > truth
        tested += 1
        plain_high += plain
        busy_high += busy
        both += plain and busy
        neither += not plain and not busy
print(f"{'rule':>22} {'graphs above the truth':>24} {'share':>8}")
print(f"{'vertices in name order':>22} {plain_high:>24} {plain_high / tested:>8.4f}")
print(f"{'busiest first':>22} {busy_high:>24} {busy_high / tested:>8.4f}")
print()
print(f"graphs tested                        : {tested}")
print(f"graphs where both rules were above   : {both}")
print(f"graphs where neither rule was above  : {neither}")

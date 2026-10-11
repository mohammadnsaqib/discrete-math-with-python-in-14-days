"""The degrees add to twice the edges, checked over every small graph."""
from itertools import combinations

from dmkit.graph import Graph, degrees

vertices = list(range(5))
possible = list(combinations(vertices, 2))
print(f"{len(vertices)} vertices give {len(possible)} possible edges "
      f"and {2 ** len(possible)} graphs")
print()
faults = 0
odd_counts = {}
for k in range(len(possible) + 1):
    for chosen in combinations(possible, k):
        g = Graph(vertices, chosen)
        d = degrees(g)
        if sum(d.values()) != 2 * len(g.edges()):
            faults += 1
        odd = sum(1 for v in vertices if d[v] % 2 == 1)
        odd_counts[odd] = odd_counts.get(odd, 0) + 1
print(f"graphs where the degrees did not add to twice the edges: {faults}")
print()
print(f"{'vertices of odd degree':>24} {'how many graphs':>17}")
for odd in sorted(odd_counts):
    print(f"{odd:>24} {odd_counts[odd]:>17}")

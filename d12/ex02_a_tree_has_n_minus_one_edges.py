"""The edge count of a tree, checked over every graph on five vertices."""
from itertools import combinations

from dmkit.graph import Graph
from dmkit.tree import has_cycle, is_tree

possible = list(combinations(range(5), 2))
counts = {}
faults = 0
for k in range(len(possible) + 1):
    for chosen in combinations(possible, k):
        g = Graph(range(5), chosen)
        if is_tree(g):
            counts[k] = counts.get(k, 0) + 1
            faults += len(g.edges()) != 4 or has_cycle(g)
print(f"graphs on 5 vertices: {2 ** len(possible)}, of which trees: "
      f"{sum(counts.values())}")
print(f"trees with a cycle or the wrong edge count: {faults}")
print(f"every tree found has this many edges: {sorted(counts)}")
print()
print(f"{'vertices':>10} {'trees on them':>15} {'n**(n-2)':>10} {'agree':>7}")
for n in range(1, 7):
    edges = list(combinations(range(n), 2))
    found = sum(is_tree(Graph(range(n), chosen))
                for k in range(len(edges) + 1)
                for chosen in combinations(edges, k))
    predicted = n ** (n - 2) if n >= 2 else 1
    print(f"{n:>10} {found:>15} {predicted:>10} {str(found == predicted):>7}")

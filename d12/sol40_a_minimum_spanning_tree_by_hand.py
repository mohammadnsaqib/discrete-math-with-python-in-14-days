"""Problem 12.27: the cheapest tree found by brute force, and by two algorithms."""
from itertools import combinations

from dmkit.induct import best_of
from dmkit.tree import all_spanning_trees, kruskal, prim, total_weight, weighted_graph


def complete_weighted(n):
    """A complete graph on n vertices with weights that repeat no pattern by accident.
    """
    return weighted_graph([(chr(97 + a), chr(97 + b), (a * 7 + b * 3) % 11 + 1)
                           for a, b in combinations(range(n), 2)])


def cheapest_by_brute_force(graph, weights):
    """The cheapest spanning tree, found by building every one of them."""
    return min((sum(weights[e] for e in t), t) for t in all_spanning_trees(graph))


print(f"{'vertices':>10} {'edges':>7} {'spanning trees':>16} {'brute force':>13} "
      f"{'Kruskal':>9} {'agree':>7} {'brute, seconds':>16} {'Kruskal, seconds':>18}")
for n in (4, 5, 6, 7):
    g, weights = complete_weighted(n)
    best, _ = cheapest_by_brute_force(g, weights)
    by_k = total_weight(kruskal(g, weights), weights)
    slow = best_of(lambda x=g, w=weights: cheapest_by_brute_force(x, w), 3)
    fast = best_of(lambda x=g, w=weights: kruskal(x, w), 3)
    print(f"{n:>10} {len(g.edges()):>7} {len(all_spanning_trees(g)):>16} {best:>13} "
          f"{by_k:>9} {str(best == by_k):>7} {slow:>16.6f} {fast:>18.6f}")
print()
g, weights = complete_weighted(6)
best, tree = cheapest_by_brute_force(g, weights)
print(f"on 6 vertices the cheapest tree costs {best}: "
      f"{' '.join(a + b for a, b in tree)}")
print(f"Kruskal gives {' '.join(a + b for a, b in kruskal(g, weights).edges())}")
print(f"Prim gives    {' '.join(a + b for a, b in prim(g, weights).edges())}")

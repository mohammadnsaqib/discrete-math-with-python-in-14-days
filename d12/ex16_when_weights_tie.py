"""Two edges of equal weight give two trees, both correct."""
from dmkit.tree import all_spanning_trees, kruskal, prim, total_weight, weighted_graph


def kruskal_by(graph, weights, key):
    """Kruskal with the tie-break rule handed in, so two rules can be compared."""
    parent = {v: v for v in graph.vertices()}

    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    chosen = []
    for a, b in sorted(graph.edges(), key=key):
        ra, rb = root(a), root(b)
        if ra != rb:
            parent[ra] = rb
            chosen.append((a, b))
    return chosen


g, weights = weighted_graph([("a", "b", 1), ("b", "c", 1), ("c", "d", 1),
                             ("d", "a", 1)])
trees = all_spanning_trees(g)
costs = sorted(sum(weights[e] for e in t) for t in trees)
by_kruskal, by_prim = kruskal(g, weights), prim(g, weights)
print("a ring of four with every weight 1")
print(f"   spanning trees: {len(trees)}, their costs {costs}")
print(f"   every one is cheapest: {len(set(costs)) == 1}")
print(f"   Kruskal gives {by_kruskal.edges()}")
print(f"   Prim gives    {by_prim.edges()}")
print(f"   the same tree: {by_kruskal.edges() == by_prim.edges()}, the same cost: "
      f"{total_weight(by_kruskal, weights) == total_weight(by_prim, weights)}")
print()
print(f"{'tie-break rule':>34} {'the tree it gives':>38} {'weight':>8}")
for name, key in [("weight, then endpoints ascending", lambda e: (weights[e], e)),
                  ("weight, then endpoints descending",
                   lambda e: (weights[e], tuple(-ord(c) for c in e))),
                  ("weight, then second endpoint first",
                   lambda e: (weights[e], (e[1], e[0])))]:
    chosen = kruskal_by(g, weights, key)
    print(f"{name:>34} {str(sorted(chosen)):>38} "
          f"{sum(weights[tuple(sorted(e))] for e in chosen):>8}")

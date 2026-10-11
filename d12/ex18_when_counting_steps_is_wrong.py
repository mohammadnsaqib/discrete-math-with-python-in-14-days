"""Day 11's shortest path on a graph whose edges do not cost the same."""
from dmkit.graph import shortest_path
from dmkit.tree import dijkstra, route_from, weighted_graph

g, weights = weighted_graph([("a", "b", 1), ("b", "c", 1), ("c", "d", 1),
                             ("a", "d", 10)])
by_steps = shortest_path(g, "a", "d")
by_cost = route_from(dijkstra(g, weights, "a")["parent"], "d")
print(f"the edges: {[(a + b, weights[(a, b)]) for a, b in g.edges()]}")
print(f"{'route':>10} {'steps':>7} {'cost':>7}")
for route in (by_steps, by_cost):
    print(f"{''.join(route):>10} {len(route) - 1:>7} "
          f"{sum(weights[tuple(sorted(p))] for p in zip(route, route[1:])):>7}")
print()
bigger, w2 = weighted_graph([("a", "b", 1), ("b", "c", 1), ("c", "d", 1),
                             ("d", "e", 1), ("a", "e", 20), ("b", "e", 9),
                             ("a", "c", 7)])
result = dijkstra(bigger, w2, "a")
print(f"{'to':>5} {'by steps':>12} {'its cost':>10} {'by cost':>12} {'its cost':>10}")
for end in bigger.vertices():
    steps = shortest_path(bigger, "a", end)
    cheap = route_from(result["parent"], end)
    step_cost = sum(w2[tuple(sorted(p))] for p in zip(steps, steps[1:]))
    print(f"{end:>5} {''.join(steps):>12} {step_cost:>10} {''.join(cheap):>12} "
          f"{result['cost'][end]:>10}")

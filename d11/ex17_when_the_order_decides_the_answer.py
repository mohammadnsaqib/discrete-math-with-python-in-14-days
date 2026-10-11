"""Two neighbour orders on one graph, and the two different trees they give."""
from dmkit.graph import Graph


def dfs_with_order(graph, start, reverse=False):
    """Depth-first search that visits neighbours in the given direction."""
    seen, order, parent = set(), [], {}
    stack = [(start, None)]
    while stack:
        v, came_from = stack.pop()
        if v in seen:
            continue
        seen.add(v)
        parent[v] = came_from
        order.append(v)
        neighbours = graph.neighbours(v)
        for n in (neighbours if reverse else reversed(neighbours)):
            if n not in seen:
                stack.append((n, v))
    return order, sorted(tuple(sorted((v, p))) for v, p in parent.items()
                         if p is not None)


g = Graph("abcdef", [("a", "b"), ("a", "c"), ("b", "d"), ("c", "d"), ("d", "e"),
                     ("e", "f"), ("c", "f")])
forward_order, forward_tree = dfs_with_order(g, "a")
backward_order, backward_tree = dfs_with_order(g, "a", reverse=True)
print(f"neighbours smallest first: {forward_order}, the tree {forward_tree}")
print(f"neighbours largest first : {backward_order}, the tree {backward_tree}")
print(f"the same order: {forward_order == backward_order}, "
      f"the same tree: {forward_tree == backward_tree}")
print()
print(f"{'start':>7} {'smallest first':>26} {'largest first':>26} {'same':>6}")
for start in g.vertices():
    one, _ = dfs_with_order(g, start)
    two, _ = dfs_with_order(g, start, reverse=True)
    print(f"{start:>7} {''.join(one):>26} {''.join(two):>26} {str(one == two):>6}")

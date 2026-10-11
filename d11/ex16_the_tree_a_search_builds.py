"""Each search leaves a tree behind, and the two trees differ."""
from collections import deque

from dmkit.graph import Graph, dfs

g = Graph("abcdef", [("a", "b"), ("a", "c"), ("b", "c"), ("b", "d"), ("c", "e"),
                     ("d", "e"), ("d", "f"), ("e", "f")])


def tree_edges(parent):
    """The edges of the tree a search built, in a fixed order."""
    return sorted(tuple(sorted((v, p))) for v, p in parent.items() if p is not None)


deep = tree_edges(dfs(g, "a")["parent"])
wide_parent, queue = {"a": None}, deque(["a"])
while queue:
    v = queue.popleft()
    for n in g.neighbours(v):
        if n not in wide_parent:
            wide_parent[n] = v
            queue.append(n)
wide = tree_edges(wide_parent)

print(f"the graph has {len(g.edges())} edges: {g.edges()}")
print(f"depth-first tree  : {deep}")
print(f"breadth-first tree: {wide}")
print(f"edges in each: {len(deep)} and {len(wide)}, the same tree: {deep == wide}")
print(f"edges in both: {sorted(set(deep) & set(wide))}")
print(f"edges the depth-first search left out: {sorted(set(g.edges()) - set(deep))}")
print()
print(f"{'start':>7} {'depth-first tree':>40}")
for start in g.vertices():
    print(f"{start:>7} {str(tree_edges(dfs(g, start)['parent'])):>40}")

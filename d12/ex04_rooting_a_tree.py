"""Choosing one vertex as the root gives every other a parent."""
from collections import deque

from dmkit.graph import Graph
from dmkit.tree import is_tree


def rooted_at(tree, root):
    """The parent and depth of every vertex, when the tree is hung from one of them."""
    parent, depth, queue = {root: None}, {root: 0}, deque([root])
    while queue:
        v = queue.popleft()
        for n in tree.neighbours(v):
            if n not in parent:
                parent[n], depth[n] = v, depth[v] + 1
                queue.append(n)
    return parent, depth


t = Graph("abcdefg", [("a", "b"), ("a", "c"), ("b", "d"), ("b", "e"), ("c", "f"),
                      ("f", "g")])
parent, depth = rooted_at(t, "a")
print(f"the tree: {t.edges()}, a tree: {is_tree(t)}")
print(f"{'vertex':>8} {'parent':>8} {'depth':>7} {'children':>18} {'a leaf':>8}")
for v in t.vertices():
    children = sorted(c for c in t.neighbours(v) if parent[c] == v)
    print(f"{v:>8} {str(parent[v]):>8} {depth[v]:>7} {str(children):>18} "
          f"{str(not children):>8}")
print()
print(f"{'root':>8} {'height':>8} {'leaves':>8}")
for root in t.vertices():
    p, d = rooted_at(t, root)
    leaves = sum(1 for v in t.vertices()
                 if not [c for c in t.neighbours(v) if p[c] == v])
    print(f"{root:>8} {max(d.values()):>8} {leaves:>8}")

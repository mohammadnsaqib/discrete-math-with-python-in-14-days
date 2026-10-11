"""The same tree hung from two different vertices."""
from collections import deque

from dmkit.graph import Graph


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


t = Graph("abcdefg", [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("c", "f"),
                      ("f", "g")])
print(f"the tree: {t.edges()}")
for root in ("a", "c"):
    parent, depth = rooted_at(t, root)
    layers = {}
    for v, d in depth.items():
        layers.setdefault(d, []).append(v)
    print(f"hung from {root}, height {max(depth.values())}: "
          + "; ".join(f"depth {d} {sorted(layers[d])}" for d in sorted(layers)))
print()
base = t.edges()
print(f"{'root':>8} {'height':>8} {'the edges are the same':>26}")
for root in t.vertices():
    parent, depth = rooted_at(t, root)
    rebuilt = sorted(tuple(sorted((v, p))) for v, p in parent.items() if p is not None)
    print(f"{root:>8} {max(depth.values()):>8} {str(rebuilt == base):>26}")

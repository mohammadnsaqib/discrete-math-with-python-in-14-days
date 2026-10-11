"""Walking a graph by following one route as far as it goes."""
from dmkit.graph import Graph, bfs, dfs

g = Graph("abcdef", [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "f"),
                     ("f", "a")])
deep = dfs(g, "a")
wide = bfs(g, "a")

print(f"the graph is a ring: {g.edges()}")
print(f"depth-first order  : {deep['order']}")
print(f"breadth-first order: {wide['order']}")
print(f"the same vertices  : {sorted(deep['order']) == sorted(wide['order'])}")
print(f"the same order     : {deep['order'] == wide['order']}")
print()
depth = {}
for v in deep["order"]:
    parent = deep["parent"][v]
    depth[v] = 0 if parent is None else depth[parent] + 1
print(f"{'vertex':>8} {'reached from':>14} {'depth in the tree':>19} "
      f"{'true distance':>15} {'same':>6}")
for v in deep["order"]:
    print(f"{v:>8} {str(deep['parent'][v]):>14} {depth[v]:>19} "
          f"{wide['distance'][v]:>15} {str(depth[v] == wide['distance'][v]):>6}")
print()
differ = [v for v in g.vertices() if depth[v] != wide["distance"][v]]
print(f"vertices where the two depths differ: {differ}")
print(f"the worst gap: {max(depth[v] - wide['distance'][v] for v in g.vertices())}")

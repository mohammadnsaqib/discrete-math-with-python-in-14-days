"""What a search does when the graph is in pieces."""
from dmkit.graph import Graph, bfs, components, dfs

g = Graph(range(9), [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (6, 7)])
print(f"the graph: {len(g.vertices())} vertices, {len(g.edges())} edges")
print(f"the pieces: {components(g)}")
print()
print(f"{'start':>7} {'breadth-first reaches':>26} {'depth-first reaches':>26} "
      f"{'same set':>10}")
for start in g.vertices():
    wide = bfs(g, start)["order"]
    deep = dfs(g, start)["order"]
    print(f"{start:>7} {str(wide):>26} {str(deep):>26} "
          f"{str(sorted(wide) == sorted(deep)):>10}")
print()
covered = []
seen = set()
for v in g.vertices():
    if v in seen:
        continue
    reached = bfs(g, v)["order"]
    seen.update(reached)
    covered.append(sorted(reached))
print(f"restarting from each unvisited vertex covers: {covered}")
print(f"that is the component list: {covered == components(g)}")

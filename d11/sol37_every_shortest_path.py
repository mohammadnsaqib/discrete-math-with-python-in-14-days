"""Problem 11.26: every shortest route in a graph, against an independent one."""
import networkx as nx

from dmkit.graph import (Graph, bfs, complete_graph, cycle_graph, path_graph,
                         shortest_path)

cases = [("a ring of 7", cycle_graph(7)), ("a line of 7", path_graph(7)),
         ("complete on 6", complete_graph(6)),
         ("a star of 6", Graph(range(6), [(0, i) for i in range(1, 6)])),
         ("two triangles joined", Graph(range(6), [(0, 1), (1, 2), (2, 0),
                                                   (3, 4), (4, 5), (5, 3), (2, 3)]))]
print(f"{'graph':>24} {'pairs':>7} {'reachable':>11} {'longest route':>15} "
      f"{'NetworkX agrees':>17}")
for name, g in cases:
    other = nx.Graph()
    other.add_nodes_from(g.vertices())
    other.add_edges_from(g.edges())
    pairs = reachable = longest = 0
    agree = True
    for a in g.vertices():
        for b in g.vertices():
            pairs += 1
            route = shortest_path(g, a, b)
            if route is None:
                agree = agree and not nx.has_path(other, a, b)
                continue
            reachable += 1
            longest = max(longest, len(route) - 1)
            agree = agree and len(route) - 1 == nx.shortest_path_length(other, a, b)
    print(f"{name:>24} {pairs:>7} {reachable:>11} {longest:>15} {str(agree):>17}")
print()
g = cases[0][1]
print("every route out of vertex 0 in a ring of 7:")
for b in g.vertices():
    print(f"   to {b}: {shortest_path(g, 0, b)}")
print(f"the distances from 0: {bfs(g, 0)['distance']}")

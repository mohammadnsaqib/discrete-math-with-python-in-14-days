"""One shortest route between two vertices, and why the queue is what makes it shortest.
"""
import networkx as nx

from dmkit.graph import Graph, bfs, shortest_path

g = Graph("abcdefg", [("a", "b"), ("a", "c"), ("b", "d"), ("c", "d"), ("c", "e"),
                      ("d", "f"), ("e", "f"), ("f", "g")])
other = nx.Graph()
other.add_nodes_from(g.vertices())
other.add_edges_from(g.edges())

print(f"{'from':>6} {'to':>4} {'route':>26} {'length':>8} {'NetworkX length':>17} "
      f"{'agree':>7}")
for start in "ab":
    for end in g.vertices():
        route = shortest_path(g, start, end)
        if route is None:
            print(f"{start:>6} {end:>4} {'none':>26} {'-':>8} {'-':>17} {'-':>7}")
            continue
        theirs = nx.shortest_path_length(other, start, end)
        print(f"{start:>6} {end:>4} {''.join(route):>26} {len(route) - 1:>8} "
              f"{theirs:>17} {str(len(route) - 1 == theirs):>7}")
print()
disconnected = Graph("abcd", [("a", "b"), ("c", "d")])
print(f"in a graph of two pieces, the route from a to c is: "
      f"{shortest_path(disconnected, 'a', 'c')}")
print(f"and from a to b it is: {shortest_path(disconnected, 'a', 'b')}")
print()
distances = bfs(g, "a")["distance"]
bad = [v for v in g.vertices()
       if len(shortest_path(g, "a", v)) - 1 != distances[v]]
print(f"vertices where the route length and the search distance differ: {bad}")

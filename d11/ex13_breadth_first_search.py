"""Walking a graph a layer at a time."""
import networkx as nx

from dmkit.graph import Graph, bfs

g = Graph("abcdefg", [("a", "b"), ("a", "c"), ("b", "d"), ("c", "d"), ("c", "e"),
                      ("d", "f"), ("e", "f"), ("f", "g")])
result = bfs(g, "a")
print(f"the order reached : {result['order']}")
print()
print(f"{'vertex':>8} {'distance from a':>17} {'neighbours':>26}")
for v in g.vertices():
    print(f"{v:>8} {result['distance'][v]:>17} {str(g.neighbours(v)):>26}")
print()
layers = {}
for v, d in result["distance"].items():
    layers.setdefault(d, []).append(v)
print("the layers:")
for d in sorted(layers):
    print(f"   distance {d}: {sorted(layers[d])}")
print()
other = nx.Graph()
other.add_nodes_from(g.vertices())
other.add_edges_from(g.edges())
theirs = nx.single_source_shortest_path_length(other, "a")
print(f"NetworkX distances : {dict(sorted(theirs.items()))}")
print(f"they match         : {result['distance'] == dict(theirs)}")

"""An edge whose removal breaks the graph in two."""
import networkx as nx

from dmkit.graph import Graph, components, cycle_graph


def bridges(graph):
    """Every edge whose removal increases the number of pieces."""
    before = len(components(graph))
    return [(a, b) for a, b in graph.edges()
            if len(components(Graph(graph.vertices(),
                                    [e for e in graph.edges()
                                     if e != (a, b)]))) > before]


cases = [("a ring of 5", cycle_graph(5)),
         ("a line of 5", Graph(range(5), [(i, i + 1) for i in range(4)])),
         ("two triangles joined", Graph(range(6), [(0, 1), (1, 2), (2, 0),
                                                   (3, 4), (4, 5), (5, 3), (2, 3)])),
         ("a triangle with a tail", Graph(range(4), [(0, 1), (1, 2), (2, 0), (2, 3)]))]
print(f"{'graph':>24} {'edges':>7} {'bridges':>9} {'NetworkX agrees':>17} "
      f"{'the bridges':>34}")
for name, g in cases:
    other = nx.Graph()
    other.add_nodes_from(g.vertices())
    other.add_edges_from(g.edges())
    mine = bridges(g)
    theirs = sorted(tuple(sorted(e)) for e in nx.bridges(other))
    print(f"{name:>24} {len(g.edges()):>7} {len(mine):>9} "
          f"{str(mine == theirs):>17} {str(mine):>34}")
print()
g = cases[2][1]
cut = bridges(g)[0]
smaller = Graph(g.vertices(), [e for e in g.edges() if e != cut])
print(f"removing the bridge {cut} from two joined triangles:")
print(f"   pieces before: {components(g)}")
print(f"   pieces after : {components(smaller)}")

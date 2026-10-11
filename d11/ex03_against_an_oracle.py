"""The book's graph against one built by a library."""
import networkx as nx

from dmkit.graph import Graph, complete_graph, cycle_graph, path_graph


def as_networkx(graph):
    """The same graph, handed to NetworkX."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    return other


print(f"{'graph':>18} {'vertices':>10} {'edges':>8} {'NetworkX vertices':>19} "
      f"{'NetworkX edges':>16} {'agree':>7}")
cases = [("complete on 6", complete_graph(6)), ("a ring of 7", cycle_graph(7)),
         ("a line of 5", path_graph(5)), ("five isolated", Graph(range(5))),
         ("one edge", Graph("ab", [("a", "b")]))]
for name, g in cases:
    other = as_networkx(g)
    agree = (len(g.vertices()) == other.number_of_nodes()
             and len(g.edges()) == other.number_of_edges())
    print(f"{name:>18} {len(g.vertices()):>10} {len(g.edges()):>8} "
          f"{other.number_of_nodes():>19} {other.number_of_edges():>16} "
          f"{str(agree):>7}")
print()
g = cycle_graph(7)
other = as_networkx(g)
print(f"the edges from the book    : {g.edges()}")
print(f"the edges from NetworkX    : {sorted(tuple(sorted(e)) for e in other.edges())}")
print(f"they match                 : "
      f"{g.edges() == sorted(tuple(sorted(e)) for e in other.edges())}")
print()
print(f"NetworkX version: {nx.__version__}")

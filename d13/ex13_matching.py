"""A set of edges no two of which touch."""
import networkx as nx

from dmkit.colour import complete_bipartite, is_matching, maximum_matching
from dmkit.graph import Graph, complete_graph, cycle_graph, path_graph


def as_networkx(graph):
    """The same graph, handed to NetworkX."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    return other


cases = [("a line of 5", path_graph(5)), ("a ring of 6", cycle_graph(6)),
         ("complete on 4", complete_graph(4)),
         ("a star of 5", Graph(range(5), [(0, i) for i in range(1, 5)])),
         ("complete 3 by 3", complete_bipartite(3, 3))]
print(f"{'graph':>18} {'vertices':>10} {'edges':>7} {'largest matching':>18} "
      f"{'NetworkX agrees':>17}")
for name, g in cases:
    mine = maximum_matching(g)
    theirs = nx.max_weight_matching(as_networkx(g), maxcardinality=True)
    print(f"{name:>18} {len(g.vertices()):>10} {len(g.edges()):>7} {len(mine):>18} "
          f"{str(len(mine) == len(theirs)):>17}")
print()
g = cases[4][1]
matching = maximum_matching(g)
print(f"complete 3 by 3: the matching is {matching}")
print(f"   a matching: {is_matching(matching)}, every vertex used: "
      f"{len({v for e in matching for v in e}) == len(g.vertices())}")
g = Graph(range(5), [(0, i) for i in range(1, 5)])
matching = maximum_matching(g)
print(f"a star of 5: the matching is {matching}, and every edge uses the centre")
print(f"   vertices left out: "
      f"{sorted(set(g.vertices()) - {v for e in matching for v in e})}")

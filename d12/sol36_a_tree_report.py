"""Problem 12.25: every fact about a tree, with an oracle beside each one."""
from itertools import combinations

import networkx as nx

from dmkit.graph import Graph, complete_graph, components, cycle_graph, path_graph
from dmkit.tree import has_cycle, is_tree


def report(graph):
    """The three properties that decide whether a graph is a tree, and a fourth that
    follows."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    one_piece = len(components(graph)) == 1
    cyclic = has_cycle(graph)
    return {"one_piece": one_piece, "no_cycle": not cyclic,
            "edges_fit": len(graph.edges()) == len(graph.vertices()) - 1,
            "tree": is_tree(graph),
            "checks": (is_tree(graph) == nx.is_tree(other)
                       and one_piece == nx.is_connected(other)
                       and cyclic == bool(list(nx.simple_cycles(other))))}


cases = [("a line of 5", path_graph(5)), ("a ring of 5", cycle_graph(5)),
         ("a star of 5", Graph(range(5), [(0, i) for i in range(1, 5)])),
         ("complete on 4", complete_graph(4)),
         ("two lines", Graph(range(6), [(0, 1), (1, 2), (3, 4), (4, 5)]))]
print(f"{'graph':>18} {'one piece':>11} {'no cycle':>10} {'edges fit':>11} "
      f"{'a tree':>8} {'checks':>8}")
for name, g in cases:
    r = report(g)
    print(f"{name:>18} {str(r['one_piece']):>11} {str(r['no_cycle']):>10} "
          f"{str(r['edges_fit']):>11} {str(r['tree']):>8} {str(r['checks']):>8}")
print()
failed = tested = misled = 0
possible = list(combinations(range(5), 2))
for k in range(len(possible) + 1):
    for chosen in combinations(possible, k):
        tested += 1
        r = report(Graph(range(5), chosen))
        failed += not r["checks"]
        misled += r["edges_fit"] and not r["tree"]
print(f"graphs on 5 vertices tested: {tested}, checks failed on: {failed}")
print(f"graphs with the right edge count that are NOT trees: {misled}")

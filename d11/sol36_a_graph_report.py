"""Problem 11.25: every structural fact about a graph, with NetworkX beside each one."""
from itertools import combinations

import networkx as nx

from dmkit.graph import (Graph, complete_graph, components, cycle_graph, degrees,
                         has_euler_circuit, path_graph)


def report(graph):
    """Facts about the graph, and whether the oracle agrees with each of them."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    d = degrees(graph)
    return {"vertices": len(graph.vertices()), "edges": len(graph.edges()),
            "pieces": len(components(graph)), "degrees_add": sum(d.values()),
            "max_degree": max(d.values(), default=0),
            "euler": has_euler_circuit(graph), "nx_euler": nx.is_eulerian(other),
            "isolated": sum(1 for v in graph.vertices() if d[v] == 0),
            "checks": (
                len(graph.vertices()) == other.number_of_nodes()
                and len(graph.edges()) == other.number_of_edges()
                and len(components(graph)) == nx.number_connected_components(other)
                and all(d[v] == other.degree(v) for v in graph.vertices())
                and sum(d.values()) == 2 * len(graph.edges()))}


cases = [("complete on 5", complete_graph(5)), ("a ring of 6", cycle_graph(6)),
         ("a line of 6", path_graph(6)), ("five isolated", Graph(range(5))),
         ("two triangles", Graph(range(6), [(0, 1), (1, 2), (2, 0),
                                            (3, 4), (4, 5), (5, 3)]))]
print(f"{'graph':>18} {'vertices':>10} {'edges':>7} {'pieces':>8} {'degrees add':>13} "
      f"{'largest':>9} {'the book':>10} {'NetworkX':>10} {'checks':>8}")
for name, g in cases:
    r = report(g)
    print(f"{name:>18} {r['vertices']:>10} {r['edges']:>7} {r['pieces']:>8} "
          f"{r['degrees_add']:>13} {r['max_degree']:>9} {str(r['euler']):>10} "
          f"{str(r['nx_euler']):>10} {str(r['checks']):>8}")
print()
failed = tested = euler_differs = with_isolated = 0
possible = list(combinations(range(5), 2))
for k in range(len(possible) + 1):
    for chosen in combinations(possible, k):
        tested += 1
        r = report(Graph(range(5), chosen))
        failed += not r["checks"]
        if r["euler"] != r["nx_euler"]:
            euler_differs += 1
            with_isolated += bool(r["isolated"])
print(f"graphs on 5 vertices tested       : {tested}")
print(f"structural checks failed on       : {failed}")
print(f"graphs where the two Euler answers differ: {euler_differs}")
print(f"of those, graphs with an isolated vertex : {with_isolated}")

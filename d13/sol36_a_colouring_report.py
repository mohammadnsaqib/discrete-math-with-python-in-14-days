"""Problem 13.25: the greedy answer, the true answer, and the gap between them."""
from itertools import combinations

import networkx as nx

from dmkit.colour import chromatic_number, greedy_colour, is_proper
from dmkit.graph import Graph, degrees


def as_networkx(graph):
    """The same graph, handed to NetworkX."""
    other = nx.Graph()
    other.add_nodes_from(graph.vertices())
    other.add_edges_from(graph.edges())
    return other


def largest_clique(graph):
    """The largest set of vertices every two of which are joined, found by search."""
    vs = graph.vertices()
    for size in range(len(vs), 0, -1):
        if any(all(b in graph.adjacency[a] for a, b in combinations(chosen, 2))
               for chosen in combinations(vs, size)):
            return size
    return 0


possible = list(combinations(range(5), 2))
tally = {}
tested = improper = broken = differ = gap = tight = nx_above = 0
for k in range(len(possible) + 1):
    for chosen in combinations(possible, k):
        g = Graph(range(5), chosen)
        colour = greedy_colour(g)
        greedy = len(set(colour.values()))
        truth = chromatic_number(g)
        clique = largest_clique(g)
        ceiling = max(degrees(g).values(), default=0) + 1
        theirs = len(set(nx.greedy_color(as_networkx(g)).values()))
        tested += 1
        improper += not is_proper(g, colour)
        broken += not clique <= truth <= greedy <= ceiling
        differ += greedy != theirs
        gap += greedy > truth
        tight += clique == truth
        nx_above += theirs > truth
        tally[(clique, truth, greedy)] = tally.get((clique, truth, greedy), 0) + 1
print(f"graphs on 5 vertices tested                      : {tested}")
print(f"greedy colourings that were improper             : {improper}")
print(f"graphs where a bound was broken                  : {broken}")
print(f"graphs where NetworkX used a different count     : {differ}")
print(f"graphs where the book's greedy is above the truth: {gap}")
print(f"graphs where NetworkX's greedy is above the truth: {nx_above}")
print(f"graphs where the clique bound is tight           : {tight}")
print()
print(f"{'clique':>8} {'the fewest':>12} {'greedy':>8} {'graphs':>8} {'share':>8}")
for key in sorted(tally):
    print(f"{key[0]:>8} {key[1]:>12} {key[2]:>8} {tally[key]:>8} "
          f"{tally[key] / tested:>8.4f}")

"""Colouring, matching and planarity. Day 13.

Three questions about a graph that all look like the ones Day 11 and Day 12 answered and
are not. Two of them have no known fast method, and this module says so by doing the
slow thing where the slow thing is the only honest thing.

THE CHROMATIC NUMBER IS FOUND BY SEARCH HERE, over every colouring with a given number
of colours. `greedy_colour` is fast and is NOT the answer: Example 13.8 prints a graph
where the greedy result is one colour worse than the truth, and the two are always
reported side by side.

ORDER DECIDES THE GREEDY ANSWER. A greedy colouring depends entirely on the order the
vertices are taken in, so the order is an argument rather than a hidden choice, and it
defaults to the vertex order that Day 11 fixed with `sorted`.
"""
from itertools import combinations, product


# --8<-- greedy_colour
def greedy_colour(graph, order=None):
    """A colouring found by giving each vertex the smallest colour its neighbours leave.

    Fast, always valid, and NOT always minimal. The order is an argument because it
    decides the answer, and Example 13.6 prints two orders on one graph giving two
    different counts.
    """
    order = graph.vertices() if order is None else list(order)
    colour = {}
    for v in order:
        taken = {colour[n] for n in graph.neighbours(v) if n in colour}
        c = 0
        while c in taken:
            c += 1
        colour[v] = c
    return colour
# --8<--


# --8<-- is_proper
def is_proper(graph, colour):
    """True when no edge has the same colour at both ends."""
    return all(colour[a] != colour[b] for a, b in graph.edges())
# --8<--


# --8<-- colourable_with
def colourable_with(graph, k):
    """A colouring using at most k colours, or None. Found by trying every assignment.

    THIS IS EXPONENTIAL AND THAT IS THE POINT. No fast method is known, and a routine
    that pretended otherwise would be a routine that returned the greedy answer under
    another name.
    """
    vs = graph.vertices()
    if not vs:
        return {}
    if k < 1:
        return None
    for assignment in product(range(k), repeat=len(vs)):
        colour = dict(zip(vs, assignment))
        if is_proper(graph, colour):
            return colour
    return None
# --8<--


# --8<-- chromatic_number
def chromatic_number(graph):
    """The fewest colours a proper colouring needs, found by searching upward from one.
    """
    vs = graph.vertices()
    if not vs:
        return 0
    for k in range(1, len(vs) + 1):
        if colourable_with(graph, k) is not None:
            return k
    return len(vs)
# --8<--


# --8<-- is_bipartite
def is_bipartite(graph):
    """True when the vertices split into two groups with every edge running between
    them.

    Checked by two-colouring rather than by searching: walk outward and give each
    neighbour the opposite colour. A clash means an odd cycle, and Example 13.11 prints
    the cycle."""
    return bipartite_parts(graph) is not None
# --8<--


# --8<-- bipartite_parts
def bipartite_parts(graph):
    """The two groups, or None when no such split exists."""
    from collections import deque
    colour = {}
    for start in graph.vertices():
        if start in colour:
            continue
        colour[start] = 0
        queue = deque([start])
        while queue:
            v = queue.popleft()
            for n in graph.neighbours(v):
                if n not in colour:
                    colour[n] = 1 - colour[v]
                    queue.append(n)
                elif colour[n] == colour[v]:
                    return None
    return (sorted(v for v in colour if colour[v] == 0),
            sorted(v for v in colour if colour[v] == 1))
# --8<--


# --8<-- maximum_matching
def maximum_matching(graph):
    """The largest set of edges sharing no vertex, found by trying every set.

    A matching is a set of edges no two of which touch. This tries the largest sizes
    first and stops at the first that works, so the answer is a maximum and not merely a
    maximal one -- Example 13.14 prints a matching that cannot be extended and is not
    the largest.
    """
    edges = graph.edges()
    for size in range(len(edges), 0, -1):
        for chosen in combinations(edges, size):
            touched = [v for e in chosen for v in e]
            if len(set(touched)) == len(touched):
                return list(chosen)
    return []
# --8<--


# --8<-- is_matching
def is_matching(edges):
    """True when no two of the edges share a vertex."""
    touched = [v for e in edges for v in e]
    return len(set(touched)) == len(touched)
# --8<--


# --8<-- greedy_matching
def greedy_matching(graph, order=None):
    """A matching built by taking edges in order and skipping any that clash.

    Always a matching, always maximal, and not always maximum. The difference between
    those two words is the whole of Example 13.14.
    """
    order = graph.edges() if order is None else list(order)
    chosen, used = [], set()
    for a, b in order:
        if a not in used and b not in used:
            chosen.append((a, b))
            used.update((a, b))
    return chosen
# --8<--


# --8<-- euler_formula_check
def euler_formula_check(vertices, edges, faces):
    """Whether a drawing satisfies vertices minus edges plus faces equals two."""
    return vertices - edges + faces == 2
# --8<--


# --8<-- edge_bound
def edge_bound(vertices, girth=3):
    """The most edges a planar graph on this many vertices can have.

    For a simple planar graph with at least 3 vertices the bound is 3n - 6, and for one
    with no triangle it is 2n - 4. Both come out of Euler's formula by counting each
    face's edges, and Example 13.18 uses them to rule out two graphs without drawing
    anything.
    """
    if vertices < 3:
        return vertices * (vertices - 1) // 2
    if girth >= 4:
        return 2 * vertices - 4
    return 3 * vertices - 6
# --8<--


def complete_bipartite(m, n):
    """The graph with m vertices on one side, n on the other, and every edge between."""
    from dmkit.graph import Graph
    left = [f"L{i}" for i in range(m)]
    right = [f"R{j}" for j in range(n)]
    return Graph(left + right, [(a, b) for a in left for b in right])

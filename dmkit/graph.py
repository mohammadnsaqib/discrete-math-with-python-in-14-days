"""Graphs, and the two ways of walking one. Day 11.

A graph is a set of vertices and a set of edges between them. Day 3 built relations,
which are sets of ordered pairs; a graph is the same object drawn rather than tabulated,
and an undirected graph is a symmetric relation.

ORDER IS FIXED EVERYWHERE IN THIS MODULE. A traversal visits neighbours in some order,
and the order decides which tree comes out. Python's `set` iterates by hash, so a
traversal built on set iteration produces a different answer for `{1, 2, 3}` than for
`{"a", "b", "c"}` and a different answer again on a machine with hash randomisation on.
Every neighbour list here is `sorted`, and the book says so wherever it prints a
traversal.

NetworkX is the oracle for every structural question. It is imported only inside the
programs that compare the two answers, never by this module, so nothing here is NetworkX
wearing another name.
"""
from itertools import combinations, permutations


# --8<-- Graph
class Graph:
    """An undirected graph, stored as a sorted neighbour list per vertex.

    Vertices are kept even when they have no edges, because a graph with an isolated
    vertex is a different graph from one without it, and a structure built only from
    edges cannot tell the two apart.
    """

    def __init__(self, vertices=(), edges=()):
        self.adjacency = {v: set() for v in vertices}
        for a, b in edges:
            self.add_edge(a, b)

    def add_vertex(self, v):
        """Add a vertex with no edges, if it is not there already."""
        self.adjacency.setdefault(v, set())

    def add_edge(self, a, b):
        """Add an edge, adding either endpoint if it is new. Loops are refused."""
        if a == b:
            raise ValueError("this graph has no loops")
        self.adjacency.setdefault(a, set()).add(b)
        self.adjacency.setdefault(b, set()).add(a)

    def vertices(self):
        """Every vertex, in a fixed order."""
        return sorted(self.adjacency)

    def edges(self):
        """Every edge once, as a sorted pair, in a fixed order."""
        return sorted({tuple(sorted((a, b)))
                       for a, neighbours in self.adjacency.items()
                       for b in neighbours})

    def neighbours(self, v):
        """The neighbours of a vertex, in a fixed order."""
        return sorted(self.adjacency[v])

    def __repr__(self):
        return f"Graph({len(self.vertices())} vertices, {len(self.edges())} edges)"
# --8<--


# --8<-- adjacency_matrix
def adjacency_matrix(graph):
    """The graph as a square of ones and zeros, rows and columns in vertex order."""
    vs = graph.vertices()
    index = {v: i for i, v in enumerate(vs)}
    matrix = [[0] * len(vs) for _ in vs]
    for a, b in graph.edges():
        matrix[index[a]][index[b]] = 1
        matrix[index[b]][index[a]] = 1
    return matrix
# --8<--


# --8<-- matrix_power
def matrix_power(matrix, power):
    """A matrix raised to a whole power, by repeated multiplication.

    The entry in row i and column j of the k-th power counts the walks of length k from
    vertex i to vertex j. That is a counting argument rather than a fact about matrices:
    each walk of length k is a walk of length k-1 followed by one edge, which is Day 5's
    product rule.
    """
    size = len(matrix)
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    for _ in range(power):
        result = [[sum(result[i][k] * matrix[k][j] for k in range(size))
                   for j in range(size)] for i in range(size)]
    return result
# --8<--


# --8<-- degrees
def degrees(graph):
    """How many edges meet each vertex, in vertex order."""
    return {v: len(graph.adjacency[v]) for v in graph.vertices()}
# --8<--


# --8<-- bfs
def bfs(graph, start):
    """Vertices in the order breadth-first search reaches them, with their distances.

    The frontier is a queue, so everything one step away is seen before anything two
    steps away. That is what makes the distances correct, and it is the whole difference
    from the next routine.
    """
    from collections import deque
    seen = {start: 0}
    order = [start]
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for n in graph.neighbours(v):
            if n not in seen:
                seen[n] = seen[v] + 1
                order.append(n)
                queue.append(n)
    return {"order": order, "distance": seen}
# --8<--


# --8<-- dfs
def dfs(graph, start):
    """Vertices in the order depth-first search reaches them, with the tree it builds.

    The frontier is a stack, so the search follows one route as far as it goes before
    trying another. It reaches the same vertices as breadth-first search and in a
    different order, and its distances are NOT shortest distances -- Example 11.15
    prints a case where they differ.
    """
    seen, order, parent = set(), [], {}
    stack = [(start, None)]
    while stack:
        v, came_from = stack.pop()
        if v in seen:
            continue
        seen.add(v)
        parent[v] = came_from
        order.append(v)
        for n in reversed(graph.neighbours(v)):
            if n not in seen:
                stack.append((n, v))
    return {"order": order, "parent": parent}
# --8<--


# --8<-- components
def components(graph):
    """The vertices split into connected groups, each sorted, groups sorted by first
    member."""
    seen, groups = set(), []
    for v in graph.vertices():
        if v in seen:
            continue
        group = sorted(bfs(graph, v)["distance"])
        seen.update(group)
        groups.append(group)
    return groups
# --8<--


# --8<-- shortest_path
def shortest_path(graph, start, end):
    """One shortest route between two vertices, or None when there is none.

    Built by breadth-first search, which is correct only because every edge counts the
    same. Day 12 meets the case where edges carry weights, and this routine is wrong
    there.
    """
    from collections import deque
    if start == end:
        return [start]
    parent = {start: None}
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for n in graph.neighbours(v):
            if n not in parent:
                parent[n] = v
                if n == end:
                    route = [end]
                    while route[-1] is not None:
                        route.append(parent[route[-1]])
                    return route[-2::-1]
                queue.append(n)
    return None
# --8<--


# --8<-- has_euler_circuit
def has_euler_circuit(graph):
    """True when a closed walk uses every edge exactly once.

    The condition is that the graph is connected on its non-isolated vertices and every
    degree is even. That is a THEOREM and not a search: walking in and out of a vertex
    uses two edges, so an odd degree strands one.

    ISOLATED VERTICES ARE IGNORED HERE, and NetworkX's `is_eulerian` does not ignore
    them: it requires the whole graph to be connected. The two therefore disagree on
    every graph with both a circuit and a vertex of degree zero, and Problem 11.25
    counts those rather than hiding them. Neither convention is wrong; the book says
    which one it uses.
    """
    used = [v for v in graph.vertices() if graph.adjacency[v]]
    if not used:
        return True
    if len(components(graph)) - (len(graph.vertices()) - len(used)) > 1:
        return False
    return all(len(graph.adjacency[v]) % 2 == 0 for v in used)
# --8<--


# --8<-- euler_circuit
def euler_circuit(graph):
    """A closed walk using every edge exactly once, or None."""
    if not has_euler_circuit(graph):
        return None
    remaining = {v: set(ns) for v, ns in graph.adjacency.items()}
    start = next((v for v in graph.vertices() if remaining[v]), None)
    if start is None:
        return []
    stack, circuit = [start], []
    while stack:
        v = stack[-1]
        if remaining[v]:
            n = min(remaining[v])
            remaining[v].discard(n)
            remaining[n].discard(v)
            stack.append(n)
        else:
            circuit.append(stack.pop())
    return circuit[::-1]
# --8<--


# --8<-- hamilton_path
def hamilton_path(graph):
    """A route visiting every vertex once, or None. Found by trying every order.

    THERE IS NO KNOWN FAST METHOD, and this routine is the honest version of that: it
    tries every arrangement of the vertices. Example 11.20 measures how far that gets
    before it stops being possible.
    """
    vs = graph.vertices()
    for order in permutations(vs):
        if all(b in graph.adjacency[a] for a, b in zip(order, order[1:])):
            return list(order)
    return None
# --8<--


def complete_graph(n):
    """The graph on n vertices with every possible edge."""
    return Graph(range(n), combinations(range(n), 2))


def cycle_graph(n):
    """The graph on n vertices forming one closed ring."""
    return Graph(range(n), [(i, (i + 1) % n) for i in range(n)])


def path_graph(n):
    """The graph on n vertices forming one open line."""
    return Graph(range(n), [(i, i + 1) for i in range(n - 1)])

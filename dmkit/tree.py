"""Trees, and the four algorithms that build or walk them. Day 12.

A tree is a connected graph with no cycle. Day 11 found that shape by accident: every
traversal left one behind, and every one had one fewer edge than the graph had vertices.
Today that is the definition rather than an observation.

WEIGHTS ARE THE NEW THING. Day 11's shortest paths were correct only because every edge
counted the same. Once edges carry a cost, the breadth-first route is wrong, and Example
12.18 prints a graph where the fewest-step route costs 10 and the cheapest costs 3.

TIES ARE BROKEN EXPLICITLY EVERYWHERE. Two edges of equal weight give two different
minimum spanning trees, both correct and both of the same total weight. A routine that
let a set decide which came first would print a different tree on a different machine,
so every choice here is made by `sorted` on the weight and then on the endpoints.
"""
from itertools import combinations

from dmkit.graph import Graph, components


# --8<-- is_tree
def is_tree(graph):
    """True when the graph is connected and has no cycle.

    Checked as two separate conditions rather than by counting edges. The edge count is
    a CONSEQUENCE -- a tree on n vertices has n-1 edges -- and using it as the test
    would report a graph made of a triangle and an isolated vertex as a tree.
    """
    if not graph.vertices():
        return False
    if len(components(graph)) != 1:
        return False
    return len(graph.edges()) == len(graph.vertices()) - 1
# --8<--


# --8<-- has_cycle
def has_cycle(graph):
    """True when some cycle exists, found by walking rather than by counting edges."""
    seen = set()
    for start in graph.vertices():
        if start in seen:
            continue
        stack = [(start, None)]
        local = set()
        while stack:
            v, came_from = stack.pop()
            if v in local:
                return True
            local.add(v)
            for n in graph.neighbours(v):
                if n != came_from and n not in local:
                    stack.append((n, v))
                elif n != came_from and n in local:
                    return True
        seen |= local
    return False
# --8<--


# --8<-- BinaryTree
class BinaryTree:
    """A value with a left and a right subtree, either of which may be missing.

    Written as a class rather than a tuple because Day 12 asks it questions -- its
    height, its leaves, its traversals -- and a tuple would answer them through free
    functions that took the shape on trust.
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def size(self):
        """How many nodes the tree holds."""
        return 1 + (self.left.size() if self.left else 0) \
                 + (self.right.size() if self.right else 0)

    def height(self):
        """The longest route from here to a leaf, counting edges."""
        if self.left is None and self.right is None:
            return 0
        return 1 + max(self.left.height() if self.left else -1,
                       self.right.height() if self.right else -1)

    def leaves(self):
        """The values at the bottom, left to right."""
        if self.left is None and self.right is None:
            return [self.value]
        return ((self.left.leaves() if self.left else [])
                + (self.right.leaves() if self.right else []))

    def __repr__(self):
        return f"BinaryTree({self.value})"
# --8<--


# --8<-- preorder
def preorder(tree):
    """The node, then the left subtree, then the right."""
    if tree is None:
        return []
    return [tree.value] + preorder(tree.left) + preorder(tree.right)
# --8<--


# --8<-- inorder
def inorder(tree):
    """The left subtree, then the node, then the right.

    For a search tree this comes out sorted, which is the reason the order has a name.
    Example 12.8 checks that against `sorted` rather than asserting it.
    """
    if tree is None:
        return []
    return inorder(tree.left) + [tree.value] + inorder(tree.right)
# --8<--


# --8<-- postorder
def postorder(tree):
    """The left subtree, then the right, then the node."""
    if tree is None:
        return []
    return postorder(tree.left) + postorder(tree.right) + [tree.value]
# --8<--


# --8<-- insert
def insert(tree, value):
    """A search tree with one more value in it, built without changing the old one."""
    if tree is None:
        return BinaryTree(value)
    if value < tree.value:
        return BinaryTree(tree.value, insert(tree.left, value), tree.right)
    return BinaryTree(tree.value, tree.left, insert(tree.right, value))
# --8<--


# --8<-- spanning_tree
def spanning_tree(graph):
    """A tree touching every vertex, built by a breadth-first walk.

    Any traversal produces one, which Day 11 noticed. This routine exists so that the
    weighted versions below have something unweighted to be compared against.
    """
    from collections import deque
    if not graph.vertices():
        return Graph()
    start = graph.vertices()[0]
    seen = {start}
    chosen = []
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for n in graph.neighbours(v):
            if n not in seen:
                seen.add(n)
                chosen.append((v, n))
                queue.append(n)
    return Graph(graph.vertices(), chosen)
# --8<--


# --8<-- kruskal
def kruskal(graph, weights):
    """A minimum spanning tree, built by taking cheap edges that join separate pieces.

    Edges are sorted by weight and then by their endpoints, so a tie is broken the same
    way on every machine. Without that second key a set would decide, and the printed
    tree would move between runs.
    """
    parent = {v: v for v in graph.vertices()}

    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    chosen = []
    for a, b in sorted(graph.edges(), key=lambda e: (weights[e], e)):
        ra, rb = root(a), root(b)
        if ra != rb:
            parent[ra] = rb
            chosen.append((a, b))
    return Graph(graph.vertices(), chosen)
# --8<--


# --8<-- prim
def prim(graph, weights, start=None):
    """A minimum spanning tree, built by growing one piece outward from a vertex.

    Kruskal takes the cheapest edge anywhere; this takes the cheapest edge leaving what
    has been built so far. The two produce trees of the same total weight and NOT always
    the same tree, which Example 12.16 prints.
    """
    vs = graph.vertices()
    if not vs:
        return Graph()
    start = vs[0] if start is None else start
    inside = {start}
    chosen = []
    while len(inside) < len(vs):
        candidates = [(weights[tuple(sorted((a, b)))], tuple(sorted((a, b))))
                      for a in inside for b in graph.neighbours(a) if b not in inside]
        if not candidates:
            break
        _, edge = min(candidates)
        chosen.append(edge)
        inside.update(edge)
    return Graph(vs, chosen)
# --8<--


# --8<-- total_weight
def total_weight(tree, weights):
    """What a set of edges costs in all."""
    return sum(weights[e] for e in tree.edges())
# --8<--


# --8<-- dijkstra
def dijkstra(graph, weights, start):
    """The cheapest route from one vertex to every other, with the routes themselves.

    Day 11's breadth-first search counted steps and was right because every edge cost
    the same. This takes the cheapest unfinished vertex at each turn instead, and
    Example 12.18 shows a graph where the two answers differ.
    """
    import heapq
    best = {start: 0}
    parent = {start: None}
    done = set()
    frontier = [(0, start)]
    while frontier:
        cost, v = heapq.heappop(frontier)
        if v in done:
            continue
        done.add(v)
        for n in graph.neighbours(v):
            step = weights[tuple(sorted((v, n)))]
            if n not in best or cost + step < best[n]:
                best[n] = cost + step
                parent[n] = v
                heapq.heappush(frontier, (best[n], n))
    return {"cost": best, "parent": parent}
# --8<--


# --8<-- route_from
def route_from(parent, end):
    """The route to a vertex, read backwards out of a parent table."""
    if end not in parent:
        return None
    route = [end]
    while parent[route[-1]] is not None:
        route.append(parent[route[-1]])
    return route[::-1]
# --8<--


def weighted_graph(edges):
    """A graph and its weights, from a list of (a, b, weight) triples."""
    g = Graph({v for a, b, _ in edges for v in (a, b)},
              [(a, b) for a, b, _ in edges])
    weights = {tuple(sorted((a, b))): w for a, b, w in edges}
    return g, weights


def all_spanning_trees(graph):
    """Every spanning tree of a small graph, found by trying every set of the right
    size."""
    vs = graph.vertices()
    wanted = len(vs) - 1
    found = []
    for chosen in combinations(graph.edges(), wanted):
        candidate = Graph(vs, chosen)
        if is_tree(candidate):
            found.append(candidate.edges())
    return found

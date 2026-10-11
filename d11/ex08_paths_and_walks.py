"""Three words for a route through a graph, and what each of them forbids."""
from dmkit.graph import Graph

g = Graph("abcde", [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a"), ("a", "c")])


def is_walk(graph, route):
    """True when every consecutive pair is an edge."""
    return all(b in graph.adjacency[a] for a, b in zip(route, route[1:]))


def is_trail(graph, route):
    """A walk that uses no edge twice."""
    used = [tuple(sorted(pair)) for pair in zip(route, route[1:])]
    return is_walk(graph, route) and len(set(used)) == len(used)


def is_path(graph, route):
    """A walk that visits no vertex twice."""
    return is_walk(graph, route) and len(set(route)) == len(route)


def routes_of_length(graph, start, length):
    """Every walk of the given length out of a vertex."""
    walks = [[start]]
    for _ in range(length):
        walks = [w + [n] for w in walks for n in graph.neighbours(w[-1])]
    return walks


print(f"{'route':>10} {'a walk':>8} {'a trail':>9} {'a path':>8}")
for route in ["abc", "abca", "abcda", "aba", "abd"]:
    print(f"{route:>10} {str(is_walk(g, list(route))):>8} "
          f"{str(is_trail(g, list(route))):>9} {str(is_path(g, list(route))):>8}")
print()
print(f"{'length':>8} {'walks from a':>14} {'trails from a':>15} {'paths from a':>14}")
for length in range(1, 5):
    walks = routes_of_length(g, "a", length)
    print(f"{length:>8} {len(walks):>14} "
          f"{len([w for w in walks if is_trail(g, w)]):>15} "
          f"{len([w for w in walks if is_path(g, w)]):>14}")

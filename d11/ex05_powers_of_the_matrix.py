"""The powers of the adjacency matrix count walks."""
from dmkit.graph import Graph, adjacency_matrix, cycle_graph, matrix_power


def walks_by_hand(graph, start, end, length):
    """Every walk of the given length between two vertices, counted by building them."""
    routes = [[start]]
    for _ in range(length):
        routes = [r + [n] for r in routes for n in graph.neighbours(r[-1])]
    return len([r for r in routes if r[-1] == end])


g = Graph("abcd", [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a")])
matrix = adjacency_matrix(g)
vs = g.vertices()
for power in (1, 2, 3):
    print(f"the matrix to the power {power}:")
    result = matrix_power(matrix, power)
    print("    " + " ".join(f"{v:>3}" for v in vs))
    for v, row in zip(vs, result):
        print(f"{v:>3} " + " ".join(f"{x:>3}" for x in row))
    print()
print(f"{'from':>6} {'to':>4} {'length':>8} {'by the matrix':>15} {'by building':>13} "
      f"{'agree':>7}")
faults = 0
for start in vs:
    for end in vs:
        for length in (1, 2, 3, 4):
            counted = matrix_power(matrix, length)[vs.index(start)][vs.index(end)]
            built = walks_by_hand(g, start, end, length)
            faults += counted != built
            if start == "a" and end in ("a", "c") and length <= 3:
                print(f"{start:>6} {end:>4} {length:>8} {counted:>15} {built:>13} "
                      f"{str(counted == built):>7}")
print()
print(f"places where the matrix and the built walks disagreed: {faults}")

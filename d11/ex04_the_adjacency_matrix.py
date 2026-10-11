"""A graph as a square of ones and zeros."""
import networkx as nx

from dmkit.graph import Graph, adjacency_matrix, complete_graph, cycle_graph

g = Graph("abcde", [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a"), ("a", "c")])
matrix = adjacency_matrix(g)
vs = g.vertices()
print("    " + " ".join(f"{v:>3}" for v in vs))
for v, row in zip(vs, matrix):
    print(f"{v:>3} " + " ".join(f"{x:>3}" for x in row))
print()
symmetric = all(matrix[i][j] == matrix[j][i]
                for i in range(len(vs)) for j in range(len(vs)))
print(f"the matrix is symmetric: {symmetric}")
print(f"the diagonal is all zero: {all(matrix[i][i] == 0 for i in range(len(vs)))}")
print(f"the entries add to {sum(sum(row) for row in matrix)}, "
      f"which is twice the {len(g.edges())} edges")
print()
print(f"{'graph':>18} {'size':>6} {'ones in the matrix':>20} {'edges':>8} "
      f"{'NetworkX agrees':>17}")
for name, built in (("complete on "
                     "4", complete_graph(4)), ("a ring of 6", cycle_graph(6)),
                    ("five isolated", Graph(range(5)))):
    m = adjacency_matrix(built)
    other = nx.Graph()
    other.add_nodes_from(built.vertices())
    other.add_edges_from(built.edges())
    ones = sum(sum(row) for row in m)
    print(f"{name:>18} {len(m):>6} {ones:>20} {len(built.edges()):>8} "
          f"{str(ones == 2 * other.number_of_edges()):>17}")

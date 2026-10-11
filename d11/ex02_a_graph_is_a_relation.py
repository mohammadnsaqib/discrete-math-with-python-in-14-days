"""An undirected graph is a symmetric relation, and the two can be built from each
other."""
from dmkit.graph import Graph
from dmkit.sets import is_reflexive, is_symmetric, is_transitive

g = Graph("abcd", [("a", "b"), ("b", "c"), ("c", "d")])
relation = {(a, b) for a in g.vertices() for b in g.neighbours(a)}

print(f"the edges       : {g.edges()}")
print(f"as a relation   : {sorted(relation)}")
print()
print(f"{'property':>16} {'holds':>7}")
print(f"{'reflexive':>16} {str(is_reflexive(relation, set(g.vertices()))):>7}")
print(f"{'symmetric':>16} {str(is_symmetric(relation)):>7}")
print(f"{'transitive':>16} {str(is_transitive(relation)):>7}")
print()
rebuilt = Graph(g.vertices(), sorted(relation))
print(f"rebuilt from the relation: {rebuilt.edges()}")
print(f"the same graph: {rebuilt.edges() == g.edges()}")
print()
print(f"{'vertices':>10} {'possible edges':>16} {'possible graphs':>18}")
for n in range(1, 7):
    possible = n * (n - 1) // 2
    print(f"{n:>10} {possible:>16} {2 ** possible:>18}")

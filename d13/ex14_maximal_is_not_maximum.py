"""A matching that cannot be extended and is still not the largest."""
from dmkit.colour import greedy_matching, is_matching, maximum_matching
from dmkit.graph import path_graph

g = path_graph(4)
print(f"a line of 4: {g.edges()}")
print(f"{'matching':>22} {'size':>6} {'a matching':>12} {'can be extended':>17}")
for name, m in (("the middle edge", [(1, 2)]), ("the largest", maximum_matching(g))):
    used = {v for e in m for v in e}
    extendable = any(a not in used and b not in used for a, b in g.edges())
    print(f"{str(m):>22} {len(m):>6} {str(is_matching(m)):>12} "
          f"{str(extendable):>17}")
print()
print(f"{'graph':>18} {'greedy matching':>17} {'largest':>9} {'greedy is best':>16}")
for n in (4, 5, 6, 7):
    built = path_graph(n)
    greedy, best = greedy_matching(built), maximum_matching(built)
    print(f"{f'a line of {n}':>18} {len(greedy):>17} {len(best):>9} "
          f"{str(len(greedy) == len(best)):>16}")
print()
print(f"a line of 4, edges in the order {g.edges()}: greedy takes {greedy_matching(g)}")
print(f"   in the order [(1, 2), (0, 1), (2, 3)]: "
      f"{greedy_matching(g, [(1, 2), (0, 1), (2, 3)])}")

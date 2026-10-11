"""What finding the true chromatic number costs as the graph grows."""
from dmkit.colour import chromatic_number, greedy_colour
from dmkit.graph import complete_graph, cycle_graph
from dmkit.induct import best_of

print(f"{'graph':>18} {'vertices':>10} {'the fewest':>12} {'seconds':>10} "
      f"{'greedy, seconds':>17}")
for n in range(3, 10):
    g = cycle_graph(n)
    slow = best_of(lambda x=g: chromatic_number(x), 3)
    fast = best_of(lambda x=g: [greedy_colour(x) for _ in range(200)], 3) / 200
    print(f"{f'a ring of {n}':>18} {n:>10} {chromatic_number(g):>12} {slow:>10.6f} "
          f"{fast:>17.8f}")
print()
print(f"{'graph':>18} {'vertices':>10} {'the fewest':>12} {'seconds':>10}")
for n in range(3, 7):
    g = complete_graph(n)
    print(f"{f'complete on {n}':>18} {n:>10} {chromatic_number(g):>12} "
          f"{best_of(lambda x=g: chromatic_number(x), 3):>10.6f}")

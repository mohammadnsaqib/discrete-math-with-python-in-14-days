"""The pigeonhole claim is about every placement, so every placement is checked."""
from itertools import product

from dmkit.counting import pigeonhole


def fullest_hole(placement, holes):
    """How many items landed in the busiest hole."""
    return max(placement.count(h) for h in range(holes))


print(f"{'items':>7} {'holes':>7} {'placements':>12} {'claimed floor':>14} "
      f"{'worst case seen':>16} {'placements below':>17}")
for items, holes in ((3, 2), (4, 3), (5, 3), (7, 3), (5, 5), (4, 5)):
    every = list(product(range(holes), repeat=items))
    floor = pigeonhole(items, holes)
    worst = min(fullest_hole(p, holes) for p in every)
    below = sum(1 for p in every if fullest_hole(p, holes) < floor)
    print(f"{items:>7} {holes:>7} {len(every):>12} {floor:>14} {worst:>16} {below:>17}")

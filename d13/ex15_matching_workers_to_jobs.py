"""Whether every job can be filled, and what stops it when it cannot."""
from itertools import combinations

from dmkit.colour import maximum_matching
from dmkit.graph import Graph


def can_fill(able):
    """A largest set of worker-job pairs with no worker or job used twice."""
    workers = sorted(able)
    jobs = sorted({j for js in able.values() for j in js})
    g = Graph(workers + jobs, [(w, j) for w, js in able.items() for j in js])
    return workers, jobs, maximum_matching(g)


cases = [
    ("everyone fits", {"Ada": ["wiring"], "Ben": ["welding"], "Cleo": ["painting"]}),
    ("a shared skill", {"Ada": ["wiring", "welding"], "Ben": ["welding"],
                        "Cleo": ["welding"]}),
    ("a full board", {"Ada": ["wiring", "welding"], "Ben": ["welding", "painting"],
                      "Cleo": ["painting", "testing"], "Dan": ["testing", "wiring"]}),
]
print(f"{'case':>18} {'workers':>9} {'jobs':>6} {'largest matching':>18} "
      f"{'all workers placed':>20}")
for name, able in cases:
    workers, jobs, matching = can_fill(able)
    placed = {v for e in matching for v in e} & set(workers)
    print(f"{name:>18} {len(workers):>9} {len(jobs):>6} {len(matching):>18} "
          f"{str(len(placed) == len(workers)):>20}")
print()
name, able = cases[1]
workers, jobs, matching = can_fill(able)
print(f"{name}: the matching is {matching}")
print(f"   left unplaced: "
      f"{sorted(set(workers) - {v for e in matching for v in e})}")
for size in range(1, len(workers) + 1):
    tight = [g for g in combinations(workers, size)
             if len({j for w in g for j in able[w]}) < size]
    if tight:
        group = tight[0]
        reachable = sorted({j for w in group for j in able[w]})
        print(f"   {list(group)} between them can do only {reachable}, which is "
              f"{len(reachable)} job for {size} workers")
        break

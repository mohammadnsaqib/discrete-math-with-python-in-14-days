"""Two-sided problems, and the split that names them."""
from dmkit.colour import bipartite_parts, complete_bipartite, is_bipartite
from dmkit.graph import Graph

# WHICH WORKER CAN DO WHICH JOB. The graph has an edge where a worker is able to do a
# job, and no edge ever runs between two workers or between two jobs.
able = {"Ada": ["wiring", "welding"], "Ben": ["welding", "painting"],
        "Cleo": ["painting"], "Dan": ["wiring", "painting", "testing"]}
workers = sorted(able)
jobs = sorted({j for js in able.values() for j in js})
g = Graph(workers + jobs, [(w, j) for w, js in able.items() for j in js])
left, right = bipartite_parts(g)

print(f"{'worker':>8} {'jobs they can do':>34}")
for w in workers:
    print(f"{w:>8} {str(g.neighbours(w)):>34}")
print()
print(f"bipartite: {is_bipartite(g)}, one side {left}")
print(f"{'':>11}the other {right}")
print(f"the sides are the workers and the jobs: "
      f"{sorted(left) == workers or sorted(right) == workers}")
print()
print(f"{'sides':>10} {'vertices':>10} {'edges':>8} {'bipartite':>11}")
for m, n in ((1, 1), (2, 3), (3, 3), (4, 2)):
    full = complete_bipartite(m, n)
    print(f"{f'{m} by {n}':>10} {len(full.vertices()):>10} "
          f"{len(full.edges()):>8} {str(is_bipartite(full)):>11}")

"""A simulation is measured against the exact value; it never replaces it."""
from dmkit.prob import probability, sample_space, simulate

space = sample_space(range(1, 7), repeat=2)
seven = lambda o: sum(o) == 7
exact = probability(space, seven)


def roll_two(rng):
    """One trial: two dice from a seeded source."""
    return (rng.randint(1, 6), rng.randint(1, 6))


print(f"the exact probability of a 7 is {exact} = {float(exact):.6f}")
print()
print(f"{'trials':>10} {'simulated':>12} {'error':>12} {'error times root n':>20}")
for runs in (100, 1000, 10000, 100000, 1000000):
    seen = simulate(roll_two, seven, runs, seed=20260910)
    error = abs(float(seen) - float(exact))
    print(f"{runs:>10} {float(seen):>12.6f} {error:>12.6f} "
          f"{error * runs ** 0.5:>20.4f}")

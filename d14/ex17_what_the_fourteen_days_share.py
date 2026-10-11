"""Four habits that ran through every day, each shown once more."""
from dmkit.colour import chromatic_number, greedy_colour
from dmkit.graph import Graph, cycle_graph
from dmkit.induct import induction_report, report_induction
from dmkit.number import factorise, is_prime_trial
from dmkit.prob import expectation, probability, sample_space, simulate

print("ONE. A search over a range refutes and never establishes.")
claim = lambda n: n * n + n + 41
print(f"   n*n + n + 41 is prime for n = 0 to 39: "
      f"{all(is_prime_trial(claim(n)) for n in range(40))}")
print(f"   at n = 40 it is {claim(40)}, which factors as {factorise(claim(40))}")
print()
print("TWO. A fast answer is printed beside the searched one, never instead of it.")
crown = Graph("abcdef", [("a", "d"), ("b", "e"), ("c", "f"), ("a", "e"), ("b", "f"),
                         ("c", "d")])
print(f"   a ring of 5: greedy uses "
      f"{len(set(greedy_colour(cycle_graph(5)).values()))}, "
      f"the fewest is {chromatic_number(cycle_graph(5))}")
print(f"   a crown of 6 in name order: "
      f"{len(set(greedy_colour(crown).values()))} colours, "
      f"in the order adefbc: {len(set(greedy_colour(crown, list('adefbc')).values()))}")
print(f"   the fewest either way: {chromatic_number(crown)}")
print()
print("THREE. An exact answer is kept exact.")
space = sample_space(range(1, 7), repeat=2)
p = probability(space, lambda o: sum(o) == 7)
seen = simulate(lambda rng: (rng.randint(1, 6), rng.randint(1, 6)),
                lambda o: sum(o) == 7, 100000, seed=20260910)
print(f"   P(two dice sum to 7) = {p}, the expected sum = {expectation(space, sum)}")
print(f"   100000 trials gave {float(seen):.6f}, which is not 1/6 and never will be")
print()
print("FOUR. A claim about every value needs an "
      "induction, and both halves are checked.")
for text, f in (("2**n is at least n**2", lambda n: 2 ** n >= n * n),
                ("n is at least 5", lambda n: n >= 5)):
    print(f"   {text}: {report_induction(induction_report(f, 1, 60))}")

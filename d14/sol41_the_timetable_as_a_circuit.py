"""Problem 14.28: the capstone timetable checked by a circuit, and counted two ways."""
from itertools import product

import networkx as nx
import sympy

from dmkit.boolean import (as_text, circuit_depth, evaluate_patterns, gate_count,
                           minimise, rows_of, truth_vector)
from dmkit.colour import chromatic_number, greedy_colour, is_proper
from dmkit.graph import Graph

wants = {"Ada": ["logic", "sets", "graphs"],
         "Ben": ["sets", "counting", "primes"],
         "Cleo": ["graphs", "trees", "colouring"],
         "Dan": ["logic", "counting", "trees"],
         "Eve": ["primes", "colouring", "graphs"]}
talks = sorted({t for wanted in wants.values() for t in wanted})
clashes = sorted({tuple(sorted((a, b))) for wanted in wants.values()
                  for a in wanted for b in wanted if a < b})
clash_graph = Graph(talks, clashes)
slots = chromatic_number(clash_graph)

# A SLOT IS TWO BITS, because four slots need two. The rule "these two talks are in
# different slots" is then a Boolean function of four inputs, and Day 14 can handle it.
vector = truth_vector(lambda p1, p0, q1, q0: (p1, p0) != (q1, q0), 4)
terms = minimise(vector, 4)
counts = gate_count(terms)
print(f"talks: {len(talks)}   clashes: {len(clashes)}   slots needed: {slots}")
print(f"the rule for one clashing pair is True on {sum(vector)} of the 16 rows")
print(f"   smallest sum of products: {as_text(terms, ['p1', 'p0', 'q1', 'q0'])}")
print(f"   gates: {counts['not']} not, {counts['and']} and, {counts['or']} or, "
      f"in {circuit_depth(terms)} layers")
print(f"   the circuit has the same column as the rule: "
      f"{tuple(evaluate_patterns(terms, row) for row in rows_of(4)) == vector}")
print(f"   {len(clashes)} copies and one and-gate to join them: "
      f"{counts['not'] + len(clashes) * (counts['and'] + counts['or']) + 1} gates")
print()
colour = greedy_colour(clash_graph)
bits = {t: (bool(colour[t] >> 1 & 1), bool(colour[t] & 1)) for t in talks}
print(f"the circuit accepts the greedy timetable: "
      f"{all(evaluate_patterns(terms, bits[a] + bits[b]) for a, b in clashes)}")
print(f"Day 13 also calls it valid              : "
      f"{is_proper(clash_graph, colour)}")
print()
other = nx.Graph()
other.add_nodes_from(talks)
other.add_edges_from(clashes)
polynomial = nx.chromatic_polynomial(other)
x = sympy.Symbol("x")
print(f"{'slots':>8} {'timetables counted one by one':>32} {'from the polynomial':>22}")
for k in range(1, 6):
    counted = sum(1 for a in product(range(k), repeat=len(talks))
                  if all(dict(zip(talks, a))[u] != dict(zip(talks, a))[v]
                         for u, v in clashes))
    print(f"{k:>8} {counted:>32} {int(polynomial.subs(x, k)):>22}")

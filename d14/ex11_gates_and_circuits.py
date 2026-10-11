"""What an expression costs when it is built out of gates."""
from dmkit.boolean import (as_text, circuit_depth, gate_count, minimise, minterms,
                           rows_of, truth_vector)

cases = [("at least two of three",
          truth_vector(lambda a, b, c: sum([a, b, c]) >= 2, 3), 3),
         ("a alone decides", truth_vector(lambda a, b, c: a, 3), 3),
         ("an odd number",
          truth_vector(lambda a, b, c: sum([a, b, c]) % 2 == 1, 3), 3),
         ("a and b agree", truth_vector(lambda a, b, c, d: a == b, 4), 4),
         ("at least two of four",
          truth_vector(lambda a, b, c, d: sum([a, b, c, d]) >= 2, 4), 4)]
print(f"{'function':>24} {'terms':>6} {'not':>5} {'and':>5} {'or':>4} {'gates':>7} "
      f"{'layers':>8} {'gates from the rows':>21}")
for name, vector, arity in cases:
    plain = [rows_of(arity)[i] for i in minterms(vector)]
    small = minimise(vector, arity)
    g = gate_count(small)
    print(f"{name:>24} {len(small):>6} {g['not']:>5} {g['and']:>5} {g['or']:>4} "
          f"{sum(g.values()):>7} {circuit_depth(small):>8} "
          f"{sum(gate_count(plain).values()):>21}")
print()
name, vector, arity = cases[0]
small = minimise(vector, arity)
g = gate_count(small)
print(f"{name}: {as_text(small, ['a', 'b', 'c'])}")
print(f"   {g['and']} AND gates and {g['or']} OR gate, in {circuit_depth(small)} "
      f"layers")
print(f"   'a alone decides' needs "
      f"{sum(gate_count(minimise(cases[1][1], 3)).values())} "
      f"gates and {circuit_depth(minimise(cases[1][1], 3))} layers")

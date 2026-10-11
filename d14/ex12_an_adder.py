"""Two circuits that add, built from their columns."""
from dmkit.boolean import (as_text, circuit_depth, gate_count, minimise, rows_of,
                           truth_vector)

half_sum = truth_vector(lambda a, b: a != b, 2)
half_carry = truth_vector(lambda a, b: a and b, 2)
full_sum = truth_vector(lambda a, b, c: (a + b + c) % 2 == 1, 3)
full_carry = truth_vector(lambda a, b, c: a + b + c >= 2, 3)

print(f"{'a':>6} {'b':>6} {'in':>6} {'sum':>6} {'carry':>7} {'a+b+in':>8}")
faults = 0
for row, s, c in zip(rows_of(3), full_sum, full_carry):
    faults += (2 if c else 0) + (1 if s else 0) != sum(row)
    print(f"{str(row[0]):>6} {str(row[1]):>6} {str(row[2]):>6} {str(s):>6} "
          f"{str(c):>7} {sum(row):>8}")
print()
print(f"rows where the two output bits did not add up to a + b + in: {faults}")
print()
outputs = [("half adder sum", half_sum, 2), ("half adder carry", half_carry, 2),
           ("full adder sum", full_sum, 3), ("full adder carry", full_carry, 3)]
print(f"{'output':>20} {'terms':>7} {'gates':>7} {'layers':>8} {'the expression':>44}")
for name, vector, arity in outputs:
    small = minimise(vector, arity)
    text = as_text(small, ["a", "b", "c"][:arity])
    shown = text if len(text) <= 44 else text[:41] + "..."
    print(f"{name:>20} {len(small):>7} {sum(gate_count(small).values()):>7} "
          f"{circuit_depth(small):>8} {shown:>44}")

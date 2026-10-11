"""A rule written in words, turned into a column and then into an expression."""
from dmkit.boolean import (evaluate_patterns, minterms, rows_of, sum_of_products,
                           truth_vector)

# THREE SENSORS AND ONE ALARM. The alarm sounds when at least two sensors agree, and
# never otherwise. That sentence is the whole specification, and it fixes the column.
alarm = lambda a, b, c: sum([a, b, c]) >= 2
vector = truth_vector(alarm, 3)
print(f"{'a':>6} {'b':>6} {'c':>6} {'alarm':>8}")
for row, value in zip(rows_of(3), vector):
    print(f"{str(row[0]):>6} {str(row[1]):>6} {str(row[2]):>6} {str(value):>8}")
print()
print(f"the True rows : {minterms(vector)}")
print(f"the expression: {sum_of_products(vector, ['a', 'b', 'c'])}")
patterns = [rows_of(3)[i] for i in minterms(vector)]
built = tuple(evaluate_patterns(patterns, row) for row in rows_of(3))
print(f"it rebuilds the column and agrees with the rule: {built == vector}")
print()
other = lambda a, b, c: (a and b) or (a and c) or (b and c)
print("a shorter rule written by hand: (a and b) or (a and c) or (b and c)")
print(f"   the same function: {truth_vector(other, 3) == vector}")

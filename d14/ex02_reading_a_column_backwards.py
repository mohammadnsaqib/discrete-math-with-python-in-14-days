"""Given a column, produce an expression that has it."""
from dmkit.boolean import evaluate_patterns, minterms, rows_of, sum_of_products

wanted = [("exactly one of a, b", (False, True, True, False)),
          ("at least one", (False, True, True, True)),
          ("both", (False, False, False, True)),
          ("never", (False, False, False, False)),
          ("always", (True, True, True, True))]
rows = rows_of(2)
print(f"{'wanted':>22} {'True rows':>12} {'rebuilt':>9} {'the expression':>32}")
for name, vector in wanted:
    patterns = [rows[i] for i in minterms(vector)]
    built = tuple(evaluate_patterns(patterns, row) for row in rows)
    print(f"{name:>22} {str(minterms(vector)):>12} {str(built == vector):>9} "
          f"{sum_of_products(vector):>32}")

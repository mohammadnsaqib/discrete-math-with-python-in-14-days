"""Every function of three inputs has a sum of products, and this builds them all."""
from itertools import product

from dmkit.boolean import evaluate_patterns, minterms, rows_of

arity = 3
rows = rows_of(arity)
faults = 0
sizes = {}
for vector in product([False, True], repeat=2 ** arity):
    patterns = [rows[i] for i in minterms(vector)]
    if tuple(evaluate_patterns(patterns, row) for row in rows) != vector:
        faults += 1
    sizes[len(patterns)] = sizes.get(len(patterns), 0) + 1
print(f"functions of {arity} inputs: {2 ** (2 ** arity)}")
print(f"functions whose sum of products did not rebuild the column: {faults}")
print()
print(f"{'True rows':>11} {'functions':>11} {'product terms needed':>22}")
for size in sorted(sizes):
    print(f"{size:>11} {sizes[size]:>11} {size:>22}")

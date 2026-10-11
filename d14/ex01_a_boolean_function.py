"""A Boolean function is its output column and nothing else."""
from dmkit.boolean import rows_of, same_function, truth_vector

functions = [
    ("a and b", lambda a, b: a and b),
    ("not (not a or not b)", lambda a, b: not (not a or not b)),
    ("a or b", lambda a, b: a or b),
    ("a != b", lambda a, b: a != b),
    ("a and not b", lambda a, b: a and not b),
]
print(f"{'expression':>24} " + " ".join(f"{str(r):>16}" for r in rows_of(2)))
for name, f in functions:
    print(f"{name:>24} " + " ".join(f"{str(v):>16}" for v in truth_vector(f, 2)))
print()
print(f"{'left':>24} {'right':>24} {'same function':>15}")
for i, (name_a, fa) in enumerate(functions):
    for name_b, fb in functions[i + 1:]:
        if truth_vector(fa, 2) == truth_vector(fb, 2):
            print(f"{name_a:>24} {name_b:>24} {'True':>15}")
print()
print(f"{'inputs':>8} {'rows':>7} {'possible functions':>20}")
for arity in range(1, 6):
    print(f"{arity:>8} {2 ** arity:>7} {2 ** (2 ** arity):>20}")

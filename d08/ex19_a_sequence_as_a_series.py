"""A sequence written as the coefficients of a power series."""
from dmkit.recur import generating_function, iterate

sequences = [
    ("all ones", [1] * 10),
    ("the counting numbers", list(range(10))),
    ("powers of 2", [2 ** n for n in range(10)]),
    ("the Fibonacci numbers", iterate([1, 1], [0, 1], 10)),
    ("the towers counts", iterate([2], [0], 10, lambda n: 1)),
]
print(f"{'sequence':>24} {'the first eight coefficients':>44}")
for name, terms in sequences:
    pairs = generating_function(terms, 8)
    print(f"{name:>24} {str([value for _, value in pairs]):>44}")
print()
print("the same sequences, written as the start of a series:")
for name, terms in sequences:
    parts = []
    for n, value in generating_function(terms, 5):
        if value == 0:
            continue
        head = "" if value == 1 and n > 0 else str(value)
        tail = "" if n == 0 else ("x" if n == 1 else f"x**{n}")
        parts.append(f"{head}{tail}" if tail else head)
    print(f"   {name:>24}: {' + '.join(parts)} + ...")

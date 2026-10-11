"""Guessing a closed form from the terms, and what the guess is worth."""
from dmkit.recur import agrees_with, iterate

cases = [
    ("a(n) = 2*a(n-1) + 1, a(0) = 0", [2], [0], lambda n: 1,
     "2**n - 1", lambda n: 2 ** n - 1),
    ("a(n) = a(n-1) + 3, a(0) = 5", [1], [5], lambda n: 3,
     "5 + 3*n", lambda n: 5 + 3 * n),
    ("a(n) = a(n-1) + n, a(0) = 0", [1], [0], lambda n: n,
     "n(n+1)/2", lambda n: n * (n + 1) // 2),
    ("a(n) = 3*a(n-1), a(0) = 4", [3], [4], None,
     "4 * 3**n", lambda n: 4 * 3 ** n),
    ("a(n) = 2*a(n-1) + 1, a(0) = 0", [2], [0], lambda n: 1,
     "2*n**2 - n", lambda n: 2 * n ** 2 - n),
]
print(f"{'recurrence':>32} {'the guess':>13} {'first disagreement':>20}")
for text, coefficients, initial, forcing, name, guess in cases:
    terms = iterate(coefficients, initial, 60, forcing)
    where = agrees_with(guess, terms, tolerance=0)
    label = "none in 0..59" if where is None else f"at n = {where}"
    print(f"{text:>32} {name:>13} {label:>20}")
print()
terms = iterate([2], [0], 8, lambda n: 1)
guess = lambda n: 2 * n ** 2 - n
print(f"{'n':>4} {'iterated':>10} {'the last guess':>16} {'agree':>7}")
for n in range(8):
    print(f"{n:>4} {terms[n]:>10} {guess(n):>16} {str(terms[n] == guess(n)):>7}")

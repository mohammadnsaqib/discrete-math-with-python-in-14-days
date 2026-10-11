"""How many solutions a congruence has, and what they are."""
from dmkit.crypto import solve_congruence
from dmkit.number import gcd

print(f"{'congruence':>26} {'gcd(a, m)':>11} {'solutions':>11} {'they are':>26}")
for a, b, m in ((3, 2, 7), (4, 2, 6), (4, 3, 6), (6, 3, 9), (2, 4, 8), (5, 1, 12)):
    answers = solve_congruence(a, b, m)
    print(f"{f'{a}x = {b} mod {m}':>26} {gcd(a, m):>11} {len(answers):>11} "
          f"{str(answers):>26}")
print()
for a, b, m in ((4, 2, 6), (6, 3, 9)):
    brute = [x for x in range(m) if a * x % m == b % m]
    print(f"{a}x = {b} mod {m}: by the routine {solve_congruence(a, b, m)}, "
          f"by testing every x {brute}")
print()
bad = [(a, b, m) for m in range(2, 30) for a in range(1, m) for b in range(m)
       if solve_congruence(a, b, m) != [x for x in range(m) if a * x % m == b % m]]
print(f"congruences below modulus 30 where the routine and a full search differ: "
      f"{len(bad)}")

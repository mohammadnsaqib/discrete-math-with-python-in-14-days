"""Problem 10.26: every linear congruence below a modulus, solved and checked."""
from dmkit.crypto import solve_congruence
from dmkit.number import gcd

print(f"{'m':>4} {'congruences':>13} {'solvable':>10} {'answers found':>15} "
      f"{'matches a full search':>23}")
for m in range(2, 16):
    total = solvable = answers = 0
    agree = True
    for a in range(1, m):
        for b in range(m):
            total += 1
            found = solve_congruence(a, b, m)
            brute = [x for x in range(m) if a * x % m == b % m]
            if found != brute:
                agree = False
            if found:
                solvable += 1
                answers += len(found)
    print(f"{m:>4} {total:>13} {solvable:>10} {answers:>15} {str(agree):>23}")
print()
print(f"{'congruence':>22} {'gcd':>5} {'answers':>9} {'they are':>28}")
for a, b, m in ((6, 4, 10), (6, 5, 10), (9, 6, 15), (14, 7, 21), (8, 4, 12)):
    found = solve_congruence(a, b, m)
    print(f"{f'{a}x = {b} mod {m}':>22} {gcd(a, m):>5} {len(found):>9} "
          f"{str(found):>28}")

"""Which congruences are solvable, counted across every small modulus."""
from dmkit.crypto import solve_congruence
from dmkit.number import gcd

print(f"{'m':>4} {'congruences':>13} {'solvable':>10} {'with one answer':>17} "
      f"{'with more':>11} {'with none':>11}")
for m in range(2, 13):
    one = many = none = 0
    for a in range(1, m):
        for b in range(m):
            answers = solve_congruence(a, b, m)
            if not answers:
                none += 1
            elif len(answers) == 1:
                one += 1
            else:
                many += 1
    total = (m - 1) * m
    print(f"{m:>4} {total:>13} {one + many:>10} {one:>17} {many:>11} {none:>11}")
print()
print(f"{'m':>4} {'values with an inverse':>24} {'they are':>34}")
for m in (7, 8, 12, 13):
    invertible = [a for a in range(1, m) if gcd(a, m) == 1]
    print(f"{m:>4} {len(invertible):>24} {str(invertible):>34}")

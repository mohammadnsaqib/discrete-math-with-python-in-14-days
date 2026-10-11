"""The book's factorisation against one written by somebody else."""
from sympy import factorint

from dmkit.number import factorise, from_factors

print(f"{'n':>10} {'the book':>44} {'agrees with SymPy':>19}")
for n in (12, 97, 360, 1024, 999983, 1000000, 2 ** 20 - 1):
    mine = factorise(n)
    theirs = sorted(factorint(n).items())
    shown = " * ".join(f"{p}**{k}" if k > 1 else str(p) for p, k in mine)
    print(f"{n:>10} {shown:>44} {str(mine == theirs):>19}")
print()
disagreements = [n for n in range(2, 20000)
                 if factorise(n) != sorted(factorint(n).items())]
print(f"integers from 2 to 19999 where the two disagree: {disagreements}")
print()
hard = 1000003 * 1000033
mine = factorise(hard)
print(f"a product of two primes: {hard}")
print(f"   the book gives  : {mine}")
print(f"   multiplied back : {from_factors(mine)}")
print(f"   SymPy gives     : {sorted(factorint(hard).items())}")

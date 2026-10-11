"""One value satisfying several congruences at once."""
from dmkit.crypto import crt

print("x = 2 mod 3, x = 3 mod 5, x = 2 mod 7")
value, modulus = crt([2, 3, 2], [3, 5, 7])
print(f"   the answer is {value} modulo {modulus}")
print(f"   check: {value} mod 3 = {value % 3}, mod 5 = {value % 5}, "
      f"mod 7 = {value % 7}")
print(f"   the next few solutions: "
      f"{[value + k * modulus for k in range(4)]}")
print()
print(f"{'congruences':>44} {'answer':>10} {'modulus':>10} {'checks out':>12}")
cases = [([1, 2], [3, 4]), ([2, 3, 2], [3, 5, 7]), ([0, 1, 2], [4, 9, 25]),
         ([5, 12, 3], [11, 13, 17])]
for remainders, moduli in cases:
    value, modulus = crt(remainders, moduli)
    ok = all(value % m == r % m for r, m in zip(remainders, moduli))
    shown = ", ".join(f"{r} mod {m}" for r, m in zip(remainders, moduli))
    print(f"{shown:>44} {value:>10} {modulus:>10} {str(ok):>12}")
print()
try:
    crt([1, 2], [4, 6])
except ValueError as problem:
    print(f"asking for moduli 4 and 6: {problem}")
print(f"   4 and 6 share a factor of 2, and x = 1 mod 4 with x = 2 mod 6 has no "
      f"answer:")
print(f"   values below 12 satisfying both: "
      f"{[x for x in range(12) if x % 4 == 1 and x % 6 == 2]}")

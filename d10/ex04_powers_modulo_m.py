"""What happens to the powers of a value when the modulus is applied at every step."""
from dmkit.crypto import order_of
from dmkit.number import gcd

m = 7
print(f"powers modulo {m}:")
print(f"{'a':>4} " + " ".join(f"{f'a**{k}':>6}" for k in range(1,
      8)) + f" {'order':>7}")
for a in range(1, m):
    powers = [pow(a, k, m) for k in range(1, 8)]
    print(f"{a:>4} " + " ".join(f"{v:>6}" for v in powers) +
          f" {str(order_of(a, m)):>7}")
print()
m = 12
print(f"powers modulo {m}:")
print(f"{'a':>4} {'gcd(a, m)':>11} " + " ".join(f"{f'a**{k}':>6}" for k in range(1,
      6)) +
      f" {'order':>7}")
for a in range(1, m):
    powers = [pow(a, k, m) for k in range(1, 6)]
    print(f"{a:>4} {gcd(a, m):>11} " + " ".join(f"{v:>6}" for v in powers) +
          f" {str(order_of(a, m)):>7}")

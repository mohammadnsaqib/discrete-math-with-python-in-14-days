"""Primality decided by trying every divisor up to the square root."""
from math import isqrt

from dmkit.number import is_prime_trial

print(f"{'n':>8} {'prime':>7} {'isqrt(n)':>10} {'divisors tried':>16} "
      f"{'smallest factor':>17}")
for n in (2, 15, 49, 97, 121, 8191, 9409):
    tried = len(range(3, isqrt(n) + 1, 2)) if n % 2 else 0
    factor = next((d for d in range(2, n) if n % d == 0), n)
    print(f"{n:>8} {str(is_prime_trial(n)):>7} {isqrt(n):>10} {tried:>16} {factor:>17}")
print()
print(f"{'n':>20} {'isqrt(n)':>12} {'int(n ** 0.5)':>15} {'agree':>7}")
checks = [10 ** 10, 10 ** 12, 10 ** 16 - 1, 10 ** 16, 10 ** 18 - 5, 10 ** 18]
for n in checks:
    print(f"{n:>20} {isqrt(n):>12} {int(n ** 0.5):>15} "
          f"{str(isqrt(n) == int(n ** 0.5)):>7}")
print()
bad = [n for n in checks if isqrt(n) != int(n ** 0.5)]
print(f"values above where the two routes disagree: {bad}")
for n in bad:
    print(f"   {n}: isqrt gives {isqrt(n)}, the floating-point route gives "
          f"{int(n ** 0.5)}")
    print(f"      and {int(n ** 0.5)} squared is {int(n ** 0.5) ** 2}, which is above "
          f"n")

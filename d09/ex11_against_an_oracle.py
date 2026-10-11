"""The book's primality test against one written by somebody else."""
from sympy import isprime

from dmkit.number import is_prime_trial

disagreements = [n for n in range(-5, 20000) if is_prime_trial(n) != isprime(n)]
print(f"integers from -5 to 19999 where the two disagree: {disagreements}")
print()
print(f"{'n':>12} {'the book':>10} {'SymPy':>8} {'agree':>7}")
for n in (-3, 0, 1, 2, 3, 4, 561, 1105, 2047, 8191, 65537, 999983, 1000000):
    print(f"{n:>12} {str(is_prime_trial(n)):>10} {str(isprime(n)):>8} "
          f"{str(is_prime_trial(n) == isprime(n)):>7}")
print()
carmichael = [561, 1105, 1729, 2465]
print("four numbers that pass a common quick test and are not prime:")
for n in carmichael:
    factor = next(d for d in range(2, n) if n % d == 0)
    print(f"   {n} = {factor} * {n // factor}, prime: {is_prime_trial(n)}")

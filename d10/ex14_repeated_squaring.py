"""Halving the exponent instead of counting down by one."""
from dmkit.crypto import mod_pow


def steps_of(exponent):
    """The bits of the exponent, and what each one costs."""
    trail = []
    while exponent > 0:
        trail.append(exponent & 1)
        exponent >>= 1
    return trail[::-1]


print(f"{'exponent':>10} {'in binary':>18} {'squarings':>11} {'multiplications':>17} "
      f"{'one at a time':>15}")
for exponent in (5, 13, 100, 1000, 65537, 10 ** 6):
    bits = steps_of(exponent)
    print(f"{exponent:>10} {''.join(str(b) for b in bits):>18} {len(bits) - 1:>11} "
          f"{sum(bits) - 1:>17} {exponent - 1:>15}")
print()
base, modulus = 7, 1009
value, result, exponent = base, 1, 13
print(f"computing {base}**13 mod {modulus} by squaring:")
while exponent:
    if exponent & 1:
        result = result * value % modulus
        print(f"   bit set: result becomes {result}")
    value = value * value % modulus
    exponent >>= 1
    if exponent:
        print(f"   square : the running base becomes {value}")
print(f"   the answer is {result}, and pow gives {pow(base, 13, modulus)}")
print()
bad = sum(1 for m in range(2, 40) for b in range(0, m) for e in range(0, 20)
          if mod_pow(b, e, m) != pow(b, e, m))
print(f"triples where the book's routine and pow disagree: {bad}")

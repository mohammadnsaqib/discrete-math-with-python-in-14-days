"""The cost of the two routes, measured at growing exponents."""
from dmkit.crypto import mod_pow
from dmkit.induct import best_of


def one_at_a_time(base, exponent, modulus):
    """The same answer, multiplying once per unit of the exponent."""
    result = 1
    for _ in range(exponent):
        result = result * base % modulus
    return result


base, modulus = 7, 1000003
print(f"{'exponent':>10} {'by squaring':>14} {'one at a time':>16} {'agree':>7}")
for exponent in (10, 1000, 100000):
    fast = mod_pow(base, exponent, modulus)
    slow = one_at_a_time(base, exponent, modulus)
    print(f"{exponent:>10} {fast:>14} {slow:>16} {str(fast == slow):>7}")
print()
# THE FAST ROUTE IS TIMED IN BATCHES. One call finishes in a few microseconds, which is
# near the floor of what the clock can resolve, so a thousand calls are timed and
# divided back down.
BATCH = 1000
print(f"{'exponent':>10} {'squaring, seconds':>19} {'one at a time, seconds':>24} "
      f"{'times faster':>14}")
for exponent in (10 ** 4, 10 ** 5, 10 ** 6):
    fast = best_of(lambda e=exponent: [mod_pow(base, e, modulus)
                                       for _ in range(BATCH)], 3) / BATCH
    slow = best_of(lambda e=exponent: one_at_a_time(base, e, modulus), 3)
    print(f"{exponent:>10} {fast:>19.8f} {slow:>24.6f} {slow / fast:>14.1f}")
print()
print(f"{'exponent':>22} {'bits':>7} {'squarings needed':>18}")
for name, exponent in (("10**6", 10 ** 6), ("10**12", 10 ** 12),
                       ("a 2048-bit key", 2 ** 2047)):
    print(f"{name:>22} {exponent.bit_length():>7} {exponent.bit_length() - 1:>18}")

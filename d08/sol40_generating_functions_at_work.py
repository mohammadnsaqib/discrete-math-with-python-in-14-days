"""Problem 8.27: four sequence operations done as series operations."""
from dmkit.recur import iterate, multiply_series

LIMIT = 12
ones = [1] * LIMIT
counting = list(range(LIMIT))
squares = [n * n for n in range(LIMIT)]
fib = iterate([1, 1], [0, 1], LIMIT)

print(f"{'operation':>34} {'the first eight coefficients':>42}")
print(f"{'the all-ones series':>34} {str(ones[:8]):>42}")
print(f"{'ones times ones':>34} {str(multiply_series(ones, ones, 8)):>42}")
print(f"{'running totals of 1, 2, 3, ...':>34} "
      f"{str(multiply_series(ones, counting, 8)):>42}")
print(f"{'running totals of the squares':>34} "
      f"{str(multiply_series(ones, squares, 8)):>42}")
print(f"{'running totals of Fibonacci':>34} "
      f"{str(multiply_series(ones, fib, 8)):>42}")
print()
running_fib = multiply_series(ones, fib, LIMIT)
print(f"{'n':>4} {'F(n)':>8} {'sum to F(n)':>13} {'F(n+2) - 1':>12} {'agree':>7}")
long_fib = iterate([1, 1], [0, 1], LIMIT + 3)
for n in range(8):
    claim = long_fib[n + 2] - 1
    print(f"{n:>4} {fib[n]:>8} {running_fib[n]:>13} {claim:>12} "
          f"{str(running_fib[n] == claim):>7}")
print()
squares_running = multiply_series(ones, squares, LIMIT)
print(f"{'n':>4} {'sum of squares':>16} {'n(n+1)(2n+1)/6':>17} {'agree':>7}")
for n in range(1, 8):
    closed = n * (n + 1) * (2 * n + 1) // 6
    print(f"{n:>4} {squares_running[n]:>16} {closed:>17} "
          f"{str(squares_running[n] == closed):>7}")

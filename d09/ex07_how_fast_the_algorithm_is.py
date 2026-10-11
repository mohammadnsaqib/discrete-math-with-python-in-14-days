"""The two forms counted against each other, and where the slow one becomes unusable."""
from dmkit.number import gcd_by_subtraction, gcd_steps

print(f"{'a':>10} {'b':>10} {'gcd':>6} {'subtractions':>14} {'remainder steps':>17} "
      f"{'times fewer':>12}")
for a, b in ((48, 18), (270, 192), (1071, 462), (10000, 3), (100000, 7),
             (1000000, 3), (832040, 514229)):
    answer, subtractions = gcd_by_subtraction(a, b)
    _, trail = gcd_steps(a, b)
    print(f"{a:>10} {b:>10} {answer:>6} {subtractions:>14} {len(trail):>17} "
          f"{subtractions / max(len(trail), 1):>12.1f}")
print()
worst = []
for k in range(4, 26):
    from dmkit.recur import iterate
    fib = iterate([1, 1], [1, 1], k + 2)
    _, trail = gcd_steps(fib[k + 1], fib[k])
    worst.append((fib[k + 1], fib[k], len(trail)))
print(f"{'a':>10} {'b':>10} {'steps':>7}")
for a, b, steps in worst[::4]:
    print(f"{a:>10} {b:>10} {steps:>7}")

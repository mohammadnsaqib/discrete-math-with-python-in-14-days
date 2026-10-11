"""The slow route, which is the one that settles arguments."""
from dmkit.recur import iterate

terms = iterate([2], [0], 21, lambda n: 1)
print(f"{'n':>4} {'a(n)':>12} {'2**n - 1':>12} {'agree':>7}")
for n in (0, 1, 5, 10, 15, 20):
    print(f"{n:>4} {terms[n]:>12} {2 ** n - 1:>12} {str(terms[n] == 2 ** n - 1):>7}")
print()
fib = iterate([1, 1], [0, 1], 31)
print(f"the Fibonacci terms 0 to 10: {fib[:11]}")
print(f"term 30 by iteration: {fib[30]}")
print()
big = iterate([1, 1], [0, 1], 101)
print(f"term 100 by iteration: {big[100]}")
print(f"that took 99 steps, one addition for each term after the two given.")

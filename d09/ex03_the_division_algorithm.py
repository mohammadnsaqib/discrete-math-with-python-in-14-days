"""One quotient and one remainder, and the window that makes them unique."""
from dmkit.number import division_algorithm

print(f"{'a':>8} {'b':>6} {'q':>6} {'r':>6} {'q*b + r':>9} {'0 <= r < b':>12}")
for a, b in ((17, 5), (17, 17), (5, 17), (0, 7), (-17, 5), (-3, 7), (100, 7)):
    q, r = division_algorithm(a, b)
    print(f"{a:>8} {b:>6} {q:>6} {r:>6} {q * b + r:>9} {str(0 <= r < b):>12}")
print()
a, b = 17, 5
print(f"other pairs with a = q*b + r for a = {a} and b = {b}:")
for q in range(1, 6):
    print(f"   q = {q}, r = {a - q * b}")
print("only one of them has a remainder in the window 0 to 4.")
print()
print(f"{'a':>8} {'b':>6} {'a // b':>8} {'a % b':>7} {'the routine':>14} {'agree':>7}")
for a, b in ((17, 5), (-17, 5), (-3, 7), (99, 100)):
    q, r = division_algorithm(a, b)
    print(f"{a:>8} {b:>6} {a // b:>8} {a % b:>7} {f'{q}, {r}':>14} "
          f"{str((q, r) == (a // b, a % b)):>7}")

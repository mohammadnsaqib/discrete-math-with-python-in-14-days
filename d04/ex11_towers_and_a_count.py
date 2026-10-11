"""A recursion whose move count is proved by induction on the recursion itself."""
from dmkit.induct import check_identity, hanoi

print(f"{'discs':>6} {'moves made':>12} {'2**n - 1':>10} {'agree':>6}")
for n in range(0, 13):
    moves = len(hanoi(n))
    print(f"{n:>6} {moves:>12} {2 ** n - 1:>10} {str(moves == 2 ** n - 1):>6}")
print()
print("the moves for three discs, in order:")
for k, (disc, src, dst) in enumerate(hanoi(3), start=1):
    print(f"   {k:>2}. disc {disc} from {src} to {dst}")
print()
bad = check_identity(lambda n: len(hanoi(n)), lambda n: 2 ** n - 1, 0, 17)
print(f"first disagreement in 0..16: {bad}")

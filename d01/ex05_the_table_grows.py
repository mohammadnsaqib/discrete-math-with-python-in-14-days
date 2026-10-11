"""Two to the n is finite, and it doubles."""
from dmkit.logic import truth_table

print(f"{'variables':>11} {'rows':>26} {'rows actually built':>21}")
for n in (1, 2, 3, 4, 8, 12, 16, 20, 30, 64):
    names = [f"x{i}" for i in range(n)]
    if n <= 12:
        built = f"{len(truth_table(lambda **kw: True, names)):,}"
    else:
        built = "not built"
    print(f"{n:>11} {2 ** n:>26,} {built:>21}")
print()
# The comparison is computed rather than asserted: at one row a nanosecond, how long
# does the last line of the table take?
seconds = 2 ** 64 / 1e9
print(f"at one row every nanosecond the last row would take {seconds / 3.15576e7:.1f} "
      f"years")
print("Nothing is wrong with the method. The "
      "method is exhaustive and that is its cost.")

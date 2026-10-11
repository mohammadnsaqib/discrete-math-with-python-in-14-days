"""One row built two ways, so neither route is checking itself."""
from math import comb

from dmkit.combin import pascal_by_addition, pascal_row

print(f"{'n':>4} {'by multiplying':>40} {'agree with adding':>19} {'library':>9}")
for n in range(0, 9):
    multiplied = pascal_row(n)
    added = pascal_by_addition(n)
    library = [comb(n, k) for k in range(n + 1)]
    print(f"{n:>4} {str(multiplied):>40} "
          f"{str(multiplied == added):>19} {str(multiplied == library):>9}")
print()
print("the triangle, with each row centred:")
width = len(" ".join(f"{v:>3}" for v in pascal_row(8)))
for n in range(0, 9):
    line = " ".join(f"{v:>3}" for v in pascal_row(n))
    print(f"   {line.center(width)}")

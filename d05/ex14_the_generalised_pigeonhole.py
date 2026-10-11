"""When there are many more items than holes, the floor rises."""
from dmkit.counting import pigeonhole

print(f"{'items':>8} {'holes':>8} {'items/holes':>14} {'floor':>8}")
for items, holes in ((10, 3), (11, 3), (12, 3), (13, 3), (100, 7), (1000, 26), (5, 12)):
    print(f"{items:>8} {holes:>8} {items / holes:>14.4f} {pigeonhole(items, holes):>8}")
print()
print("the floor is the quotient rounded UP, and rounding down is the common error.")
print(f"{'10 over 3':>14} rounds down to {10 // 3} and up to {pigeonhole(10, 3)}")
print(f"{'12 over 3':>14} rounds down to {12 // 3} and up to {pigeonhole(12, 3)}")

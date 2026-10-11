"""A set has no order and no repeats, and both facts are visible in what it does."""
from dmkit.sets import as_text

written = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
s = set(written)
print(f"written down : {written}")
print(f"as a set     : {as_text(s)}")
print(f"members      : {len(written)} written, {len(s)} distinct")
print()
same = [{1, 2, 3}, {3, 2, 1}, {1, 1, 2, 3}, {2, 3, 1, 3}]
print("four sets written four ways:")
for t in same:
    print(f"   {as_text(t)}")
print(f"all equal: {all(t == same[0] for t in same)}")

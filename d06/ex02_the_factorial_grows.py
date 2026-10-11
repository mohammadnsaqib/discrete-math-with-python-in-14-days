"""How fast the count of arrangements outruns the size of the collection."""
from dmkit.combin import factorial_of

print(f"{'items':>8} {'arrangements':>34} {'digits':>8} {'times the row above':>20}")
previous = None
for n in (1, 5, 10, 15, 20, 25, 30):
    value = factorial_of(n)
    ratio = "-" if previous is None else f"{value / previous:.3e}"
    print(f"{n:>8} {value:>34} {len(str(value)):>8} {ratio:>20}")
    previous = value
print()
seconds_in_a_year = 60 * 60 * 24 * 365
print(f"{'items':>8} {'seconds to build at a million a second':>40}")
for n in (10, 15, 20, 25):
    seconds = factorial_of(n) / 1000000
    unit = (f"{seconds:.1f} seconds" if seconds < seconds_in_a_year
            else f"{seconds / seconds_in_a_year:.3e} years")
    print(f"{n:>8} {unit:>40}")

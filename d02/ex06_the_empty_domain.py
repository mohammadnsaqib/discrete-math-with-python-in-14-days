"""Over an empty domain every universal claim holds and every existential one fails."""
from dmkit.proof import exists, for_all

empty = []
claims = [
    ("every member is even", lambda n: n % 2 == 0),
    ("every member is odd", lambda n: n % 2 == 1),
    ("every member is both", lambda n: n % 2 == 0 and n % 2 == 1),
]
print(f"{'claim':>28} {'for all':>9} {'there exists':>14}")
for text, pred in claims:
    found = exists(pred, empty)
    print(f"{text:>28} {str(for_all(pred, empty)):>9} {str(found is not None):>14}")

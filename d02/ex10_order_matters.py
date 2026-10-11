"""One relation, four ways of quantifying it, four different claims."""
from dmkit.proof import exists, for_all

people = ["ann", "bob", "cal"]
# who admires whom, as a set of pairs
admires = {("ann", "bob"), ("bob", "cal"), ("cal", "bob"), ("ann", "cal")}

claims = [
    ("everybody admires somebody",
     for_all(lambda x: exists(lambda y: (x, y) in admires, people) is not None,
     people)),
    ("somebody admires everybody",
     exists(lambda x: for_all(lambda y: (x, y) in admires, people),
     people) is not None),
    ("somebody is admired by everybody",
     exists(lambda y: for_all(lambda x: (x, y) in admires, people),
     people) is not None),
    ("everybody is admired by somebody",
     for_all(lambda y: exists(lambda x: (x, y) in admires, people) is not None,
     people)),
]
print("the pairs:", ", ".join(f"{a}->{b}" for a, b in sorted(admires)))
print()
for text, value in claims:
    print(f"{text:>34}: {value}")

"""Events combine the way sets do, because events are sets."""
from dmkit.prob import probability, sample_space

space = sample_space(range(1, 7), repeat=2)
seven = lambda o: sum(o) == 7
doubles = lambda o: o[0] == o[1]

rows = [
    ("the sum is 7", seven),
    ("both match", doubles),
    ("either", lambda o: seven(o) or doubles(o)),
    ("both at once", lambda o: seven(o) and doubles(o)),
    ("not 7", lambda o: not seven(o)),
    ("7 but not a double", lambda o: seven(o) and not doubles(o)),
]
print(f"{'event':>22} {'probability':>13} {'as a decimal':>14}")
for text, event in rows:
    p = probability(space, event)
    print(f"{text:>22} {str(p):>13} {float(p):>14.6f}")
print()
a = probability(space, seven)
b = probability(space, doubles)
both = probability(space, lambda o: seven(o) and doubles(o))
either = probability(space, lambda o: seven(o) or doubles(o))
print(f"{a} + {b} - {both} = {a + b - both}, and 'either' is {either}")
print(f"1 - {a} = {1 - a}, and 'not 7' is {probability(space, lambda o: not seven(o))}")

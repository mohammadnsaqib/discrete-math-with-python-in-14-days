"""Three events, independent two at a time and not all three together."""
from dmkit.prob import independent, probability, sample_space

space = sample_space("HT", repeat=2)
first_head = lambda o: o[0] == "H"
second_head = lambda o: o[1] == "H"
same = lambda o: o[0] == o[1]

events = [("first is heads", first_head), ("second is heads", second_head),
          ("the two match", same)]
print(f"{'A':>18} {'B':>18} {'P(A)P(B)':>10} {'P(A and B)':>12} {'independent':>13}")
for i, (a_name, a) in enumerate(events):
    for b_name, b in events[i + 1:]:
        pa, pb = probability(space, a), probability(space, b)
        both = probability(space, lambda o: a(o) and b(o))
        print(f"{a_name:>18} {b_name:>18} {str(pa * pb):>10} {str(both):>12} "
              f"{str(independent(space, a, b)):>13}")
print()
all_three = probability(space, lambda o: first_head(o) and second_head(o) and same(o))
product = 1
for _, e in events:
    product *= probability(space, e)
print(f"P(all three) is {all_three}")
print(f"P(A)P(B)P(C) is {product}")
print(f"they agree: {all_three == product}")

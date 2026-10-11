"""Two everyday systems that are modular arithmetic and nothing else."""


def clock(start, hours, size=12):
    """Where a clock hand lands after some hours."""
    return (start + hours) % size or size


def check_digit(digits):
    """The last digit of an identifier, chosen so a weighted sum is 0 modulo 10.

    The weights alternate 1 and 3 down the number. That choice is not decoration: it
    catches every single-digit error and almost every swap of two neighbours, and this
    example counts how many of each it catches.
    """
    total = sum(d * (3 if i % 2 else 1) for i, d in enumerate(reversed(digits)))
    return (10 - total % 10) % 10


print(f"{'start':>7} {'hours':>7} {'lands on':>10}")
for start, hours in ((9, 4), (9, 16), (3, 24), (11, 100)):
    print(f"{start:>7} {hours:>7} {clock(start, hours):>10}")
print()
body = [9, 7, 8, 0, 3, 0, 6, 4, 0, 6, 1, 5]
digit = check_digit(body)
weighted = sum(d * (3 if i % 2 else 1)
               for i, d in enumerate(reversed(body + [digit])))
print(f"the body of an identifier: {body}")
print(f"the check digit that makes the weighted sum 0 modulo 10: {digit}")
print(f"the weighted sum of the whole thing: {weighted}, modulo 10: {weighted % 10}")
print()
tried = caught = 0
for position in range(len(body)):
    for wrong in range(10):
        if wrong == body[position]:
            continue
        tried += 1
        damaged = list(body)
        damaged[position] = wrong
        caught += check_digit(damaged) != digit
swaps = caught_swaps = 0
for i in range(len(body) - 1):
    if body[i] == body[i + 1]:
        continue
    swaps += 1
    damaged = list(body)
    damaged[i], damaged[i + 1] = damaged[i + 1], damaged[i]
    caught_swaps += check_digit(damaged) != digit
print(f"single-digit changes tried: {tried}, caught: {caught}")
print(f"neighbour swaps tried: {swaps}, caught: {caught_swaps}")

"""What a game is worth, computed rather than felt."""
from dmkit.prob import expectation, probability, sample_space

two = sample_space(range(1, 7), repeat=2)

games = [
    ("pay 1, win 5 on a sum of 7", lambda o: 5 - 1 if sum(o) == 7 else -1),
    ("pay 1, win 6 on a sum of 7", lambda o: 6 - 1 if sum(o) == 7 else -1),
    ("pay 1, win 4 on a double", lambda o: 4 - 1 if o[0] == o[1] else -1),
    ("pay 1, win the sum", lambda o: sum(o) - 1),
    ("pay 4, win the larger die", lambda o: max(o) - 4),
]
print(f"{'game':>30} {'expected gain':>15} {'as a decimal':>14} {'verdict':>10}")
for text, payoff in games:
    e = expectation(two, payoff)
    verdict = "worth it" if e > 0 else ("fair" if e == 0 else "a loss")
    print(f"{text:>30} {str(e):>15} {float(e):>14.6f} {verdict:>10}")
print()
p7 = probability(two, lambda o: sum(o) == 7)
fair_prize = 1 / p7
print(f"P(sum is 7) is {p7}, so a fair prize for a stake of 1 is {fair_prize}")
gain = expectation(two, lambda o: fair_prize - 1 if sum(o) == 7 else -1)
print(f"and paying 1 to win {fair_prize} gives an expected gain of {gain}")

"""Probability as a count divided by a count, which needs the outcomes to be equally
likely."""
from dmkit.prob import probability, sample_space

coins = sample_space("HT", repeat=3)
print(f"the {len(coins)} outcomes of three coins: {[''.join(o) for o in coins]}")
print()
print(f"{'event':>26} {'outcomes':>10} {'probability':>13} {'as a decimal':>14}")
for heads in range(0, 4):
    event = lambda o, h=heads: o.count("H") == h
    hits = len([o for o in coins if event(o)])
    p = probability(coins, event)
    print(f"{f'exactly {heads} heads':>26} {hits:>10} {str(p):>13} {float(p):>14.6f}")
added = sum(probability(coins, lambda o, h=h: o.count("H") == h) for h in range(4))
print()
print(f"the four probabilities add to {added}")

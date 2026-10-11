"""The set of everything that can happen, built and printed."""
from dmkit.prob import sample_space

one_die = sample_space(range(1, 7))
two_coins = sample_space("HT", repeat=2)
three_coins = sample_space("HT", repeat=3)
two_dice = sample_space(range(1, 7), repeat=2)

print(f"one die       : {len(one_die)} outcomes, {[o[0] for o in one_die]}")
print(f"two coins     : {len(two_coins)} outcomes, {[''.join(o) for o in two_coins]}")
print(f"three coins   : {len(three_coins)} outcomes")
print(f"   {[''.join(o) for o in three_coins]}")
print(f"two dice      : {len(two_dice)} outcomes")
print(f"   the first eight: {two_dice[:8]}")
print()
print(f"{'experiment':>16} {'outcomes per trial':>20} {'trials':>8} "
      f"{'sample space':>14}")
for name, outcomes, repeat in (("one die", 6, 1), ("two coins", 2, 2),
                               ("three coins", 2, 3), ("two dice", 6, 2),
                               ("five dice", 6, 5)):
    print(f"{name:>16} {outcomes:>20} {repeat:>8} {outcomes ** repeat:>14}")

"""The commonest error in the subject: counting the wrong things as equally likely."""
from fractions import Fraction

from dmkit.prob import probability, sample_space

space = sample_space(range(1, 7), repeat=2)
sums = sorted(set(sum(o) for o in space))

print(f"{'sum':>6} {'outcomes':>10} {'true probability':>18} "
      f"{'if sums were equal':>20} {'off by':>10}")
for total in sums:
    hits = len([o for o in space if sum(o) == total])
    true = probability(space, lambda o, t=total: sum(o) == t)
    wrong = Fraction(1, len(sums))
    print(f"{total:>6} {hits:>10} {str(true):>18} {str(wrong):>20} "
          f"{float(true - wrong):>10.4f}")
print()
print(f"the eleven sums are NOT equally likely: {len(sums)} sums over {len(space)} "
      f"outcomes")
print(f"the outcomes summing to 2 : {[o for o in space if sum(o) == 2]}")
print(f"the outcomes summing to 7 : {[o for o in space if sum(o) == 7]}")

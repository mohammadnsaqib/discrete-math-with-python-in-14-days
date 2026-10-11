"""Problem 1.28: what the doubling costs on a claim somebody might actually make."""
from dmkit.logic import assignments, evaluate


def all_different(**kw):
    """A statement that no assignment of the same value to every variable satisfies."""
    values = list(kw.values())
    return any(v != values[0] for v in values)


print("A statement over n switches: 'not all of them agree'.")
print()
print(f"{'switches':>10} {'rows':>16} {'rows until a witness':>22} "
      f"{'share looked at':>17}")
for n in (4, 8, 12, 16, 20):
    names = [f"s{i}" for i in range(n)]
    looked = 0
    for a in assignments(names):
        looked += 1
        if evaluate(all_different, a):
            break
    print(f"{n:>10} {2 ** n:>16,} {looked:>22,} {looked / 2 ** n:>16.6%}")

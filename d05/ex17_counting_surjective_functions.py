"""The count that needs inclusion and exclusion rather than a single product."""
from math import comb

from dmkit.counting import enumerate_check, functions_from
from dmkit.sets import is_surjective


def onto_count(domain, codomain):
    """How many functions from a domain of one size land on every member of the other.

    Count every function, remove those that miss at least one target, and put back what
    the removal took twice. That is Section 5.4's alternation applied to a set of
    functions rather than to a set of numbers.
    """
    return sum((-1) ** k * comb(codomain, k) * (codomain - k) ** domain
               for k in range(codomain + 1))


print(f"{'domain':>8} {'codomain':>10} {'by the rule':>13} {'by building':>13} "
      f"{'agree':>7}")
for domain in range(1, 6):
    for codomain in range(1, 4):
        dom = list(range(domain))
        cod = list("abc"[:codomain])
        counted = onto_count(domain, codomain)
        result = enumerate_check(
            counted,
            lambda d=dom,
            c=cod: [f for f in functions_from(d, c) if is_surjective(f,
            c)],
            "")
        print(f"{domain:>8} {codomain:>10} {counted:>13} {result['built']:>13} "
              f"{str(result['agree']):>7}")

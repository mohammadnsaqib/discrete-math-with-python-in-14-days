"""The counting rules, and the enumeration every one of them is checked against. Day 5.

A counting rule is a claim that a collection has a certain size WITHOUT building it.
That is the whole value of counting: the collections are large, and building one to
measure it defeats the purpose.

It is also the whole danger. A formula that is off by one, or that quietly counts an
ordered thing as unordered, produces a number that looks exactly as plausible as the
right one. So every rule in this module has `enumerate_check` beside it, and every count
printed in Day 5 is run against a list that was actually built. Where the collection is
too large to build, the rule is checked on a smaller case first and the size is then
reported without enumeration -- and the book says which of the two happened.
"""
from itertools import product


# --8<-- sum_rule
def sum_rule(*sizes):
    """The size of a union of collections that share no member.

    THE CONDITION IS NOT DECORATION. Adding the sizes counts a shared member twice, and
    the sum rule says nothing at all about overlapping collections.
    `inclusion_exclusion` is the rule for those, and Example 5.2 shows the two answers
    differing.
    """
    return sum(sizes)
# --8<--


# --8<-- product_rule
def product_rule(*sizes):
    """The number of ways to make one independent choice from each collection in turn.

    Independent means the options at each stage do not depend on what was chosen
    earlier. Where they do -- a second choice that cannot repeat the first -- the count
    is a partial permutation instead, and Day 6 handles it.
    """
    result = 1
    for s in sizes:
        result *= s
    return result
# --8<--


# --8<-- complement_rule
def complement_rule(total, unwanted):
    """The count of what is left when the unwanted cases are removed from the whole.

    Counting the complement is often far less work than counting the thing itself: `at
    least one` has many shapes and `none` has one. The rule is only correct when
    `unwanted` counts within the same whole, which is where its mistakes come from.
    """
    return total - unwanted
# --8<--


# --8<-- inclusion_exclusion
def inclusion_exclusion(*sets):
    """The size of a union of overlapping collections, by alternating addition and
    subtraction.

    Add the sizes, subtract every pairwise overlap, add back every triple overlap, and
    so on. The alternation is not a trick: a member of three of the collections is
    counted three times by the first term and removed three times by the second, so the
    third term is what puts it back exactly once.
    """
    from itertools import combinations
    total = 0
    for k in range(1, len(sets) + 1):
        for group in combinations(sets, k):
            shared = set(group[0])
            for s in group[1:]:
                shared &= set(s)
            total += (-1) ** (k + 1) * len(shared)
    return total
# --8<--


# --8<-- pigeonhole
def pigeonhole(items, holes):
    """The smallest number of items that must share a hole, when items are placed in
    holes.

    The claim is not about a clever placement. It holds for EVERY placement, which is
    what makes it a proof rather than an observation, and Example 5.12 checks it against
    every placement of a small case."""
    if holes <= 0:
        raise ValueError("there must be at least one hole")
    return -(-items // holes)
# --8<--


# --8<-- count_functions
def count_functions(domain, codomain):
    """How many functions run from a domain of one size into a codomain of another.

    Each member of the domain is sent somewhere, independently of the rest, so this is
    the product rule with the same factor repeated. Day 3 built the functions
    themselves; this counts them without building them.
    """
    return codomain ** domain
# --8<--


# --8<-- enumerate_check
def enumerate_check(counted, build, description):
    """Compare a formula's answer against a collection that was actually built.

    THIS IS THE GATE THE WHOLE DAY RUNS THROUGH. A counting formula is a claim about a
    size, and the only honest check on it is to build the collection and measure it.
    `build` is a function of no arguments returning the collection; its length is the
    truth, and `counted` is the claim.
    """
    built = list(build())
    return {"description": description, "counted": counted, "built": len(built),
            "agree": counted == len(built),
            "sample": built[:4]}
# --8<--


# --8<-- report_count
def report_count(result):
    """One line saying whether a formula matched the collection it claims to size."""
    verdict = "agree" if result["agree"] else "DISAGREE"
    return (f"{result['description']:>34} {result['counted']:>12} "
            f"{result['built']:>12}  {verdict}")
# --8<--


def strings_over(alphabet, length):
    """Every string of the given length over the given alphabet, in a fixed order."""
    return ["".join(t) for t in product(sorted(alphabet), repeat=length)]


def functions_from(domain, codomain):
    """Every function from a domain into a codomain, as a list of pair lists, in a fixed
    order."""
    dom, cod = sorted(domain), sorted(codomain)
    return [list(zip(dom, outs)) for outs in product(cod, repeat=len(dom))]

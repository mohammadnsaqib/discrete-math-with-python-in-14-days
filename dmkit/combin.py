"""Arrangements and selections, and the four cases they divide into. Day 6.

Two questions decide every count in this chapter. Does the ORDER matter? May an item be
used MORE THAN ONCE? Four answers, four formulas, and picking the wrong one gives a
number that looks as reasonable as the right one.

Every routine here is written from its definition rather than called out to a library,
and every one is checked twice in Day 6: against `math.perm`, `math.comb` or
`sympy.expand`, and against a collection built with `itertools`. A formula that agrees
with a library and disagrees with a built collection has caught a misunderstanding
rather than a typing error, and that is the more interesting of the two.
"""
from itertools import permutations


# --8<-- factorial_of
def factorial_of(n):
    """n!, the number of ways to arrange n distinct items, computed by multiplying up.

    It is written out rather than imported so that Day 6 can point at the multiplication
    and say where each factor comes from: the first position has n choices, the second
    n-1, and so on down to one.
    """
    if n < 0:
        raise ValueError("there is no factorial of a negative number")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result
# --8<--


# --8<-- permutations_count
def permutations_count(n, k=None):
    """Arrangements of k items chosen from n, where the order matters and nothing
    repeats.

    The product runs n, n-1, ... for k factors, and stops. Writing it as n! over (n-k)!
    is the same number and hides that the cancelling factors were never needed."""
    k = n if k is None else k
    if k > n:
        return 0
    result = 1
    for i in range(k):
        result *= n - i
    return result
# --8<--


# --8<-- combinations_count
def combinations_count(n, k):
    """Selections of k items from n, where the order does NOT matter and nothing
    repeats.

    Every selection of k items can be arranged in k! ways, and the arrangement count
    above produced all of them. Dividing by k! collapses each group of arrangements to
    the one selection behind it, and Example 6.7 prints the group before it is
    collapsed."""
    if k < 0 or k > n:
        return 0
    return permutations_count(n, k) // factorial_of(k)
# --8<--


# --8<-- binomial
def binomial(n, k):
    """The same number under the name it carries in the binomial theorem.

    It is the count of k-member subsets of an n-member set, and it is the coefficient of
    x**k in the expansion of (1 + x)**n. Those are the same number for one reason, which
    Section 6.5 gives.
    """
    return combinations_count(n, k)
# --8<--


# --8<-- pascal_row
def pascal_row(n):
    """One row of the triangle, built from the row above by adding neighbours.

    Each entry is the sum of the two above it because a k-member subset of n items
    either contains the last item or does not. That is a proof rather than a pattern,
    and the routine is written to make the two additions visible.
    """
    row = [1]
    for k in range(1, n + 1):
        row.append(row[-1] * (n - k + 1) // k)
    return row
# --8<--


# --8<-- pascal_by_addition
def pascal_by_addition(n):
    """The same row, built only by adding, with no multiplication or division anywhere.

    This is the independent route the multiplied row is checked against in Example 6.13.
    Two routes to one row is the only way to tell a correct formula from a plausible
    one.
    """
    row = [1]
    for _ in range(n):
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
    return row
# --8<--


# --8<-- combinations_with_repetition
def combinations_with_repetition(n, k):
    """Selections of k items from n kinds, order ignored, repeats allowed.

    The count is the number of ways to place k identical marks into n labelled boxes,
    which is the number of ways to arrange k marks and n-1 dividers in a row. Example
    6.16 prints the dividers rather than describing them.
    """
    if n == 0:
        return 1 if k == 0 else 0
    return combinations_count(n + k - 1, k)
# --8<--


# --8<-- multiset_permutations
def multiset_permutations(counts):
    """Arrangements of items where some are identical, given how many of each there are.

    Arrange everything as though distinct, then divide by the arrangements WITHIN each
    group of identical items, because those produce the same word. Example 6.18 shows
    one word arriving several times before the division.
    """
    total = factorial_of(sum(counts))
    for c in counts:
        total //= factorial_of(c)
    return total
# --8<--


# --8<-- expand_binomial
def expand_binomial(n):
    """The coefficients of (a + b)**n, from the counting argument rather than by
    multiplying.

    Each term of the expansion picks a or b from each of the n brackets. A term with k
    copies of b comes from choosing which k brackets supplied it, and there are
    `binomial(n, k)` ways to do that. The coefficient IS the count of subsets.
    """
    return [binomial(n, k) for k in range(n + 1)]
# --8<--


# --8<-- distinct_arrangements
def distinct_arrangements(items):
    """Every distinct arrangement of the items, in a fixed order, repeats removed.

    `itertools.permutations` treats equal items as different, so a word with a repeated
    letter comes back several times. Removing the repeats and sorting gives the
    collection that `multiset_permutations` claims to size.
    """
    return sorted(set(permutations(items)))
# --8<--

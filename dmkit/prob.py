"""Probability over a finite sample space, computed exactly. Day 7.

Every probability in this chapter is a count divided by a count. Day 5 and Day 6 built
the counting; this module divides, and it divides with `Fraction` rather than with
floating point.

THAT CHOICE IS NOT FUSSINESS. A third is not representable in binary, and a chapter that
prints 0.30000000000000004 where it means three tenths has spent its credibility on
nothing. Fractions also make an identity visible: two routes to one probability agree
exactly or they do not agree, with no tolerance to argue about.

A simulation appears here twice, and it is never the answer. It is measured AGAINST the
exact value, so the reader sees how far a hundred thousand trials gets and how far it
does not.
"""
from fractions import Fraction
from itertools import product


# --8<-- sample_space
def sample_space(outcomes, repeat=1):
    """Every outcome of repeating one experiment, in a fixed order.

    The order is fixed by `sorted` rather than by set iteration, for the reason Day 3
    gave: a printed sample space has to come out the same on two runs and on two
    machines.
    """
    return [t for t in product(sorted(outcomes), repeat=repeat)]
# --8<--


# --8<-- probability
def probability(space, event):
    """The exact probability of an event over an equally likely sample space.

    `event` is a function from an outcome to True or False, so an event is a QUESTION
    rather than a list. That is what lets the same routine handle 'at least one six' and
    'the sum is seven' without either being written out.
    """
    if not space:
        raise ValueError("an empty sample space has no probabilities")
    return Fraction(sum(1 for outcome in space if event(outcome)), len(space))
# --8<--


# --8<-- conditional
def conditional(space, event, given):
    """The probability of an event among the outcomes where another one held.

    The sample space SHRINKS to the outcomes satisfying `given`, which is the whole
    content of conditioning. Example 7.10 prints both spaces so the shrinking is visible
    rather than described.
    """
    reduced = [outcome for outcome in space if given(outcome)]
    if not reduced:
        raise ValueError("cannot condition on an event that never happens")
    return probability(reduced, event)
# --8<--


# --8<-- independent
def independent(space, first, second):
    """True when knowing one event happened does not change the other's probability.

    Checked as an equation on three probabilities rather than by intuition, because
    intuition is wrong about this more often than about anything else in the chapter.
    """
    both = probability(space, lambda o: first(o) and second(o))
    return both == probability(space, first) * probability(space, second)
# --8<--


# --8<-- bayes
def bayes(prior, likelihood, false_positive):
    """The probability of the cause given the evidence, from the three numbers usually
    known.

    `prior` is how common the cause is, `likelihood` how often the evidence appears when
    the cause is present, and `false_positive` how often it appears when the cause is
    absent. The answer is often far below what people expect, and Example 7.16 shows
    why: the absent case is much larger, so even a small rate on it produces many cases.
    """
    with_cause = prior * likelihood
    without_cause = (1 - prior) * false_positive
    total = with_cause + without_cause
    if total == 0:
        raise ValueError("the evidence never appears under either hypothesis")
    return with_cause / total
# --8<--


# --8<-- expectation
def expectation(space, value):
    """The average of a quantity over an equally likely sample space, exactly.

    `value` maps an outcome to a number. The result is a Fraction, so an expected value
    of seven halves prints as 7/2 rather than as 3.5000000000000004.
    """
    if not space:
        raise ValueError("an empty sample space has no expectation")
    return Fraction(sum(Fraction(value(o)) for o in space), len(space))
# --8<--


# --8<-- variance
def variance(space, value):
    """The average squared distance from the mean, exactly.

    Computed from the definition rather than as the mean of the squares minus the square
    of the mean. The two are equal in exact arithmetic and Example 7.20 checks that they
    are; they are NOT equal in floating point, which is one reason this module avoids
    it.
    """
    mean = expectation(space, value)
    return expectation(space, lambda o: (Fraction(value(o)) - mean) ** 2)
# --8<--


# --8<-- simulate
def simulate(trial, event, runs, seed=0):
    """The share of runs in which an event happened, from a seeded pseudo-random source.

    THE SEED IS FIXED so the book prints the same number twice. This routine never
    produces an answer in this chapter: it produces something to compare against the
    answer, and Example 7.8 measures how far it gets.
    """
    import random
    rng = random.Random(seed)
    hits = sum(1 for _ in range(runs) if event(trial(rng)))
    return Fraction(hits, runs)
# --8<--


def as_text(fraction, places=6):
    """A fraction printed both exactly and as a decimal, for a table."""
    return f"{fraction} = {float(fraction):.{places}f}"

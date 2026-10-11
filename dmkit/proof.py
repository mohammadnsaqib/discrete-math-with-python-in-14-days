"""Quantifiers over a finite domain, and the four ways a claim gets settled. Day 2.

Day 1's tables decided everything because a statement of n variables has 2**n rows and
that is finite. Today the domain stops being finite, and exactly one thing survives the
change:

    A COUNTEREXAMPLE STILL SETTLES A "FOR ALL" CLAIM, AND NOTHING ELSE DOES.

Finding one member of the domain where the claim fails refutes it, whatever the size of
the domain. Finding none over the first million members refutes nothing and establishes
nothing. Every routine here is built so that the difference is visible in what it
returns: a refutation comes back with the witness that produced it, and a confirmation
comes back with the range it covered and no verdict at all.
"""


# --8<-- for_all
def for_all(predicate, domain):
    """True when the predicate holds for every member of the domain.

    HOW MUCH THIS IS WORTH DEPENDS ENTIRELY ON THE DOMAIN, and the routine cannot tell.
    Over `range(2, 100)` the answer is a decision. Over the first hundred of infinitely
    many integers it is a report about a hundred integers, and `check_over` below is the
    honest way to say so.
    """
    return all(predicate(x) for x in domain)
# --8<--


# --8<-- exists
def exists(predicate, domain):
    """The first member of the domain satisfying the predicate, or None.

    The member comes back rather than a boolean, for the reason Day 1 gave: a claim that
    something exists is checkable in one step when the witness comes with it, and is
    worth nothing when it does not.
    """
    for x in domain:
        if predicate(x):
            return x
    return None
# --8<--


# --8<-- counterexample
def counterexample(predicate, domain):
    """The first member of the domain where the predicate FAILS, or None.

    This is the one routine in the module whose positive answer is a proof. A returned
    value refutes the universal claim outright and a reader can substitute it and see.
    `None` means only that the search finished without finding one -- which is why it is
    never reported on its own, and why `check_over` exists.
    """
    for x in domain:
        if not predicate(x):
            return x
    return None
# --8<--


# --8<-- check_over
def check_over(predicate, domain, description):
    """Search a range, and report what the search did rather than a verdict.

    The returned dictionary has no `True` in it anywhere when the search finds nothing.
    It has the count examined and the description of the range, because that is the
    whole content of what happened. A routine that returned `True` here would be
    inviting the reader to write "and so it holds for every integer", which is the
    mistake Day 2 exists to prevent.
    """
    checked = 0
    for x in domain:
        checked += 1
        if not predicate(x):
            return {"refuted": True, "witness": x, "checked": checked,
                    "range": description}
    return {"refuted": False, "witness": None, "checked": checked,
            "range": description}
# --8<--


# --8<-- report
def report(result):
    """One line saying exactly what a search established, and no more than that."""
    if result["refuted"]:
        return (f"REFUTED by {result['witness']!r}, found after "
                f"{result['checked']} of {result['range']}")
    # ASCII only. A program's OUTPUT becomes a fenced block in the book, and a fenced
    # block is reproduced byte for byte; an em dash there depends on the console
    # encoding of whoever runs it rather than on the program.
    return (f"no counterexample in {result['checked']} of {result['range']} -- "
            f"this settles nothing about the rest")
# --8<--


# --8<-- divides
def divides(a, b):
    """True when a divides b with no remainder. Day 9 builds on this one."""
    return a != 0 and b % a == 0
# --8<--


def is_even(n):
    """True when n is even. Written out because Day 2 proves things about it."""
    return n % 2 == 0


def is_odd(n):
    """True when n is odd."""
    return n % 2 == 1


# --8<-- is_prime_slow
def is_prime_slow(n):
    """Primality by trial division, written for certainty rather than for speed.

    Day 9 replaces it. It is here because Day 2 needs a predicate whose truth is not
    obvious from looking at the number, and because every claim about primes in this
    chapter has to be checked against something that cannot be doubted.
    """
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True
# --8<--


# --8<-- direct_check
def direct_check(hypothesis, conclusion, domain):
    """Every member where the hypothesis holds, and whether the conclusion held there
    too.

    This is what a direct proof does one case at a time, done over a finite range. The
    count of members where the hypothesis was vacuous is returned separately, because a
    conditional claim confirmed only on members that never satisfied its hypothesis has
    been confirmed by nothing at all -- and that is a real way to be misled."""
    tested = vacuous = failures = 0
    first_failure = None
    for x in domain:
        if hypothesis(x):
            tested += 1
            if not conclusion(x):
                failures += 1
                if first_failure is None:
                    first_failure = x
        else:
            vacuous += 1
    return {"tested": tested, "vacuous": vacuous, "failures": failures,
            "first_failure": first_failure}
# --8<--

"""Recurrences, and the closed forms that sometimes replace them. Day 8.

A recurrence defines each term from earlier ones. Day 4 met several and solved none of
them: it proved that a closed form was right once somebody had guessed it. Today
produces the closed form instead of guessing.

TWO ROUTES RUN THROUGH THE WHOLE CHAPTER AND THEY MUST NEVER SHARE A STEP. One iterates
the recurrence, which is slow, correct by construction, and settles any argument. The
other solves it algebraically, which is fast and takes one slip to ruin. Every closed
form here is checked against the iteration, and several are checked against SymPy's
`rsolve` as well.

Floating point appears only where an irrational root forces it, and every such value is
compared with a tolerance that is stated rather than assumed.
"""
from fractions import Fraction


# --8<-- iterate
def iterate(coefficients, initial, limit, forcing=None):
    """The terms of a linear recurrence, computed by applying it over and over.

    `coefficients` are the multipliers of the previous terms, nearest first: `[2, 1]`
    means each term is twice the one before plus the one before that. `forcing` is an
    optional function of n added at each step, which is what makes a recurrence
    nonhomogeneous.

    THIS IS THE ORACLE FOR THE WHOLE CHAPTER. It is not clever and it cannot be wrong.
    """
    terms = list(initial)
    while len(terms) < limit:
        n = len(terms)
        value = sum(c * terms[n - 1 - i] for i, c in enumerate(coefficients))
        if forcing is not None:
            value += forcing(n)
        terms.append(value)
    return terms[:limit]
# --8<--


# --8<-- characteristic_roots
def characteristic_roots(coefficients):
    """The roots of the characteristic equation, for a recurrence of order one or two.

    For `a(n) = p*a(n-1) + q*a(n-2)` the equation is `x**2 - p*x - q = 0`. The roots are
    returned as exact Fractions when the discriminant is a perfect square, and as floats
    otherwise -- and the caller is told which by the type it gets back.
    """
    if len(coefficients) == 1:
        return [Fraction(coefficients[0])]
    if len(coefficients) != 2:
        raise ValueError("only orders one and two are solved here")
    p, q = coefficients
    discriminant = p * p + 4 * q
    root = _exact_sqrt(discriminant)
    if root is not None:
        return sorted({Fraction(p + root, 2), Fraction(p - root, 2)})
    if discriminant < 0:
        raise ValueError("the roots are not real; this "
                         "chapter does not handle that case")
    from math import sqrt
    s = sqrt(discriminant)
    return sorted({(p + s) / 2, (p - s) / 2})
# --8<--


def _exact_sqrt(value):
    """The integer square root of a perfect square, or None."""
    if value < 0:
        return None
    root = int(round(value ** 0.5))
    for candidate in (root - 1, root, root + 1):
        if candidate >= 0 and candidate * candidate == value:
            return candidate
    return None


# --8<-- solve_linear
def solve_linear(coefficients, initial):
    """The constants of the closed form, found by solving for the initial terms.

    The closed form of a second-order recurrence with distinct roots r and s is `A*r**n
    + B*s**n`. Two initial terms give two equations in A and B, and this solves them. A
    REPEATED ROOT NEEDS A DIFFERENT SHAPE, and this raises rather than returning a wrong
    answer -- `solve_repeated` is the routine for that case.
    """
    roots = characteristic_roots(coefficients)
    if len(coefficients) == 1:
        return [Fraction(initial[0])], roots
    if len(roots) == 1:
        raise ValueError("the roots are repeated; use solve_repeated")
    r, s = roots
    a0, a1 = initial
    denominator = s - r
    b = (a1 - r * a0) / denominator
    a = a0 - b
    return [a, b], roots
# --8<--


# --8<-- solve_repeated
def solve_repeated(coefficients, initial):
    """The constants when the characteristic equation has one root twice.

    The shape is `(A + B*n) * r**n` rather than `A*r**n + B*r**n`, because the second is
    only `(A+B)*r**n` and cannot match two independent initial terms. Example 8.11 shows
    the wrong shape failing before this one is introduced.
    """
    roots = characteristic_roots(coefficients)
    if len(roots) != 1:
        raise ValueError("the roots are distinct; use solve_linear")
    r = roots[0]
    a0, a1 = initial
    a = Fraction(a0) if isinstance(r, Fraction) else float(a0)
    b = a1 / r - a
    return [a, b], roots
# --8<--


# --8<-- closed_form
def closed_form(constants, roots, repeated=False):
    """A function of n built from the constants and roots, ready to be checked term by
    term."""
    if repeated:
        a, b = constants
        r = roots[0]
        return lambda n: (a + b * n) * r ** n
    if len(constants) == 1:
        a = constants[0]
        r = roots[0]
        return lambda n: a * r ** n
    a, b = constants
    r, s = roots
    return lambda n: a * r ** n + b * s ** n
# --8<--


# --8<-- agrees_with
def agrees_with(formula, terms, tolerance=1e-9):
    """The first index where a closed form and a list of terms disagree, or None.

    A tolerance is needed only when a root is irrational and the formula is computed in
    floating point. It is an ARGUMENT rather than a constant inside, so a caller
    comparing exact Fractions can pass 0 and get an exact comparison.
    """
    for n, term in enumerate(terms):
        got = formula(n)
        if tolerance == 0:
            if got != term:
                return n
        elif abs(float(got) - float(term)) > tolerance * max(1.0, abs(float(term))):
            return n
    return None
# --8<--


# --8<-- divide_conquer
def divide_conquer(subproblems, factor, extra, base, limit):
    """The cost of a divide-and-conquer method, at the sizes it actually reaches.

    `T(n) = subproblems * T(n // factor) + extra(n)`, computed only at powers of
    `factor`, because those are the sizes where the division is exact and the recurrence
    says anything. Sizes between them are interpolated by every textbook and by nothing
    here.
    """
    costs = {1: base}
    size = factor
    while size <= limit:
        costs[size] = subproblems * costs[size // factor] + extra(size)
        size *= factor
    return costs
# --8<--


# --8<-- master_theorem
def master_theorem(subproblems, factor, power):
    """Which of the three cases a divide-and-conquer recurrence falls into.

    The comparison is between `subproblems` and `factor**power`, which is the whole
    content of the theorem: how the work of splitting compares with the work at the top.
    The routine returns the case and the growth, and Example 8.17 checks the growth by
    measuring it.
    """
    split = factor ** power
    if subproblems > split:
        from math import log
        exponent = log(subproblems) / log(factor)
        return {"case": 1, "growth": f"n**{exponent:.4f}", "exponent": exponent}
    if subproblems == split:
        return {"case": 2, "growth": f"n**{power} log n", "exponent": float(power)}
    return {"case": 3, "growth": f"n**{power}", "exponent": float(power)}
# --8<--


# --8<-- generating_function
def generating_function(terms, limit=None):
    """The coefficients of a series, which is another name for the sequence itself.

    A generating function is a bookkeeping device: the sequence written as the
    coefficients of a power series, so that operations on sequences become operations on
    series. This routine does nothing but present the terms that way; Section 8.8 does
    the operations.
    """
    limit = len(terms) if limit is None else limit
    return [(n, terms[n]) for n in range(min(limit, len(terms)))]
# --8<--


# --8<-- multiply_series
def multiply_series(left, right, limit):
    """The product of two power series, to a given number of terms.

    The coefficient of x**n in a product is the sum over all ways to split n between the
    two series, which is Day 5's product rule and sum rule together. That is why a
    generating function turns a counting argument into an algebraic one.
    """
    out = []
    for n in range(limit):
        out.append(sum(left[k] * right[n - k]
                       for k in range(n + 1)
                       if k < len(left) and n - k < len(right)))
    return out
# --8<--

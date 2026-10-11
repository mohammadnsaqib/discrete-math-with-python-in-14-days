"""Induction, and the recursion it licenses. Day 4.

Day 2 said a search over a range establishes nothing about the rest. Induction is the
one way past that for the natural numbers, and it works by making a claim about ALL of
them out of two claims about finitely much: that it holds at the start, and that each
value passes it to the next.

Nothing in this module proves anything. A proof is written by a person. What is here is
the machinery for checking a proof's two halves separately over a range, because the two
halves fail in different ways and a check that reports one number cannot say which
failed.
"""
from functools import lru_cache


# --8<-- induction_report
def induction_report(claim, start, limit):
    """Check the base case and the step separately, and report them separately.

    THE TWO HALVES FAIL DIFFERENTLY AND A SINGLE NUMBER HIDES THAT. A claim can pass its
    step at every value and be false everywhere because the base case fails -- Example
    4.5 prints one. A claim can hold at the base and fail at one step, and then be false
    from that point on. The report keeps them apart because the repairs are not the same
    repair.
    """
    base = bool(claim(start))
    step_failures = []
    for n in range(start, limit):
        if claim(n) and not claim(n + 1):
            step_failures.append(n)
    return {"base": base, "base_at": start,
            "step_failures": step_failures,
            "first_step_failure": step_failures[0] if step_failures else None,
            "checked": limit - start}
# --8<--


# --8<-- report_induction
def report_induction(result):
    """One line saying which of the two halves held, and where the other stopped."""
    base = "base holds" if result["base"] else f"BASE FAILS at {result['base_at']}"
    if result["step_failures"]:
        step = (f"step FAILS first at {result['first_step_failure']} "
                f"({len(result['step_failures'])} failures)")
    else:
        step = f"step holds across {result['checked']} values"
    return f"{base}; {step}"
# --8<--


# --8<-- check_identity
def check_identity(left, right, start, limit):
    """The first value where two formulas disagree, or None.

    Used throughout Day 4 to check a closed form against the sum it claims to equal. It
    is Day 2's counterexample search under another name, and it settles the same one
    thing: a disagreement refutes, and an agreement over a range does not establish.
    """
    for n in range(start, limit):
        if left(n) != right(n):
            return n
    return None
# --8<--


# --8<-- fib_recursive
def fib_recursive(n):
    """The Fibonacci numbers, written exactly as their definition reads.

    Its cost is the thing to notice. Computing F(n) recomputes F(n-2) twice, F(n-3)
    three times, and so on, so the count of calls is itself a Fibonacci number -- which
    grows like 1.618 to the n. Example 4.16 counts the calls rather than describing
    them.
    """
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)
# --8<--


# --8<-- fib_memo
@lru_cache(maxsize=None)
def fib_memo(n):
    """The same definition, with each value computed once and kept.

    Nothing about the recursion changed. One decorator turns a count of calls that grows
    like 1.618 to the n into one that grows like n, and Example 4.16 measures both.
    """
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)
# --8<--


# --8<-- fib_iterative
def fib_iterative(n):
    """The same numbers, computed forwards, keeping two values at a time.

    This is what the recursion does once the repeats are removed, written out. It is the
    reference the other two are checked against, because it is the one whose cost is
    obvious.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
# --8<--


# --8<-- hanoi
def hanoi(n, source="A", target="C", spare="B"):
    """Every move needed to shift n discs, in order.

    The recursion is the proof: to move n, move n-1 out of the way, move the largest,
    and move the n-1 back. That the count of moves is 2**n - 1 is then an induction with
    the recursion as its step, and Example 4.11 checks the two against each other.
    """
    if n == 0:
        return []
    return (hanoi(n - 1, source, spare, target)
            + [(n, source, target)]
            + hanoi(n - 1, spare, target, source))
# --8<--


# --8<-- count_calls
def count_calls(fn):
    """Wrap a function so its calls are counted, without changing what it returns.

    Cost is measured in this book rather than described, and a count of calls is the
    honest measurement for a recursion: it does not move between machines the way a
    stopwatch does.
    """
    state = {"calls": 0}

    def wrapped(*args, **kwargs):
        state["calls"] += 1
        return fn(*args, **kwargs)

    wrapped.calls = state
    return wrapped
# --8<--


def sum_to(n):
    """1 + 2 + ... + n, computed by adding them up."""
    return sum(range(1, n + 1))


def closed_sum(n):
    """The closed form n(n+1)/2, which Example 4.4 checks against sum_to."""
    return n * (n + 1) // 2


def collatz_steps(n, limit=1000):
    """How many steps n takes to reach 1 under the Collatz rule, or None past the limit.

    It is here because Day 4 needs one recursion whose termination nobody has proved.
    Every other routine in this module terminates for a reason that can be written down
    in a line.
    """
    steps = 0
    while n != 1 and steps < limit:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps if n == 1 else None


# --8<-- best_of
def best_of(fn, repeats=5):
    """The shortest of several runs of fn, in seconds.

    The shortest run is the one least disturbed by the rest of the machine. A mean would
    fold in every interruption, and an interruption is not a property of the algorithm.
    Day 4 uses this only to confirm what the call counts already say.
    """
    from time import perf_counter
    best = None
    for _ in range(repeats):
        t0 = perf_counter()
        fn()
        elapsed = perf_counter() - t0
        best = elapsed if best is None else min(best, elapsed)
    return best
# --8<--

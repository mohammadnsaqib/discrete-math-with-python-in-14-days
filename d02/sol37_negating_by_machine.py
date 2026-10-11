"""Problem 2.26: build the negation of a quantified claim and check both."""
from dmkit.proof import exists, for_all, is_prime_slow

dom = list(range(2, 60))


def both_ways(text, predicate):
    """Evaluate a universal claim and its negation, and confirm exactly one holds."""
    universal = for_all(predicate, dom)
    witness = exists(lambda x: not predicate(x), dom)
    negation = witness is not None
    print(f"{text:>42}")
    print(f"{'':>10}for all      : {universal}")
    print(f"{'':>10}exists not-P : {negation}"
          + (f", witnessed by {witness}" if negation else ""))
    print(f"{'':>10}exactly one  : {universal != negation}")
    print()


both_ways("every integer from 2 to 59 is prime", is_prime_slow)
both_ways("every integer from 2 to 59 is above 1", lambda n: n > 1)
both_ways("every integer from 2 to 59 is composite", lambda n: not is_prime_slow(n))

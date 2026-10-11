"""Sets, the relations built from them, and the functions that are a special case. Day
3.

A set is a collection with no order and no repeats. A relation is a set of ordered
pairs. A function is a relation in which each input appears exactly once. Everything
today is one of those three, and every property of them is a check over a finite
collection -- which is Day 1's method applied to something other than truth values.

ORDER IS FIXED EVERYWHERE IN THIS MODULE, and that is not tidiness. Python's `set`
iterates in an order that depends on the hash of what is in it, so a power set built
from `set` iteration comes out in a different order for `{1, 2, 3}` than for `{"a", "b",
"c"}` and in a different order again on a machine with hash randomisation enabled. A
book that prints one has to be able to print the same one twice."""
from itertools import chain, combinations, product


# --8<-- power_set
def power_set(s):
    """Every subset of s, in a fixed order: by size, and within a size, by the given
    order.

    There are 2**len(s) of them, which is Day 1's count again and for the same reason:
    each member is independently in or out. Day 5 uses that matching to count things
    that are not sets at all."""
    items = sorted(s)
    return [frozenset(c) for k in range(len(items) + 1)
            for c in combinations(items, k)]
# --8<--


# --8<-- cartesian
def cartesian(a, b):
    """Every ordered pair with a first member from a and a second from b.

    Its size is the product of the two sizes, which is Day 5's product rule met early.
    The pairs are ORDERED: (1, 2) and (2, 1) are different members, and that is the
    whole difference between a product and a union.
    """
    return [(x, y) for x in sorted(a) for y in sorted(b)]
# --8<--


# --8<-- is_reflexive
def is_reflexive(relation, domain):
    """True when every member of the domain is related to itself.

    The DOMAIN is an argument and not inferred from the pairs, because reflexivity is a
    claim about the domain. A relation with no pairs at all is reflexive over the empty
    domain and not over any other, and inferring the domain from the pairs would hide
    that.
    """
    return all((x, x) in relation for x in domain)
# --8<--


# --8<-- is_symmetric
def is_symmetric(relation):
    """True when every pair's reverse is also present."""
    return all((y, x) in relation for x, y in relation)
# --8<--


# --8<-- is_transitive
def is_transitive(relation):
    """True when a route of two steps is always also a route of one.

    The check is over pairs of pairs, so it costs the square of the relation's size. Day
    11 meets the same question as reachability in a graph, where it is answered by
    walking rather than by checking every pair.
    """
    return all((x, w) in relation
               for x, y in relation for z, w in relation if y == z)
# --8<--


# --8<-- is_antisymmetric
def is_antisymmetric(relation):
    """True when no two DIFFERENT members are related both ways.

    This is not the opposite of symmetric, and reading it as the opposite is the usual
    mistake. A relation can be both -- equality is -- and a relation can be neither.
    """
    return all(x == y for x, y in relation if (y, x) in relation)
# --8<--


# --8<-- transitive_closure
def transitive_closure(relation):
    """The smallest transitive relation containing the given one.

    Add every two-step route as a one-step route, and repeat until nothing new appears.
    That it terminates is not obvious and is worth stating: the relation only ever
    grows, and it cannot grow past the product of the domain with itself, which is
    finite.
    """
    closure = set(relation)
    while True:
        new = {(x, w) for x, y in closure for z, w in closure if y == z}
        if new <= closure:
            return closure
        closure |= new
# --8<--


# --8<-- equivalence_classes
def equivalence_classes(relation, domain):
    """The domain split into groups by an equivalence relation, in a fixed order.

    Each group is everything related to one member. The groups come back sorted by their
    smallest member so that two runs print the same thing, and every member appears in
    exactly one -- which is what makes an equivalence relation worth its own name.
    """
    seen, classes = set(), []
    for x in sorted(domain):
        if x in seen:
            continue
        group = sorted(y for y in domain if (x, y) in relation)
        seen.update(group)
        classes.append(group)
    return classes
# --8<--


# --8<-- is_function
def is_function(pairs, domain):
    """True when every member of the domain appears exactly once as a first member."""
    firsts = [x for x, _ in pairs]
    return all(firsts.count(x) == 1 for x in domain) and len(firsts) == len(domain)
# --8<--


# --8<-- is_injective
def is_injective(pairs):
    """True when no two inputs share an output."""
    outs = [y for _, y in pairs]
    return len(set(outs)) == len(outs)
# --8<--


# --8<-- is_surjective
def is_surjective(pairs, codomain):
    """True when every member of the codomain is an output.

    The CODOMAIN is an argument, for the same reason the domain was above: surjectivity
    is a claim about a codomain, and the same set of pairs is onto one codomain and not
    another. A routine that inferred it from the outputs would report True always.
    """
    return set(y for _, y in pairs) == set(codomain)
# --8<--


def is_bijective(pairs, domain, codomain):
    """True when the pairs are a function that is both injective and surjective."""
    return (is_function(pairs, domain) and is_injective(pairs)
            and is_surjective(pairs, codomain))


# --8<-- compose
def compose(f, g):
    """The pairs of g applied after f: (x, z) whenever f has (x, y) and g has (y, z)."""
    return sorted((x, z) for x, y in f for w, z in g if y == w)
# --8<--


def as_text(s):
    """A set printed in a fixed order, so two runs show the same thing."""
    items = sorted(s)
    return "{" + ", ".join(str(i) for i in items) + "}" if items else "{}"

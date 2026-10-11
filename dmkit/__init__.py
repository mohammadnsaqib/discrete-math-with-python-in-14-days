"""dmkit -- the discrete mathematics library built across the fourteen days of this book.

Every routine here is written in a chapter, run in that chapter, and checked against an
independent implementation before the chapter ends. Nothing is imported from SymPy or
NetworkX at run time: they appear in the book only as oracles, in programs that compare
the two answers.

Module      Day   What it holds
------      ---   -------------
logic       1     truth tables, tautology, equivalence, normal forms, satisfiability
proof       2     quantifiers over a finite domain, counterexample search, the proof patterns
sets        3     power sets, products, relations and their properties, closures, functions
induct      4     induction reports, recursion, memoisation, structural recursion
counting    5     the sum and product rules, inclusion-exclusion, the pigeonhole principle
combin      6     permutations, combinations, binomial coefficients, the four counting cases
prob        7     sample spaces, conditional probability, Bayes, expectation and variance
recur       8     iterating a recurrence, characteristic roots, closed forms, the master theorem
number      9     divisibility, the Euclidean algorithm, primes, the sieve, factorisation
crypto      10    modular inverses, the Chinese remainder theorem, totient, RSA
graph       11    graphs, degrees, breadth-first and depth-first search, Euler and Hamilton
tree        12    trees, traversals, spanning trees, Kruskal, Prim, Dijkstra
colour      13    greedy and exact colouring, bipartiteness, matching, planarity
boolean     14    Boolean functions, sum of products, minimisation, finite state machines

ONE RULE RUNS THROUGH ALL OF IT. Wherever a routine's answer depends on the order its
input is walked in -- a colouring, a traversal, a factorisation, a spanning tree -- that
order is fixed here explicitly, with `sorted()` rather than set iteration. The oracle
each is checked against made a different choice, and a book that prints one of these
answers has to be able to say which order produced it.
"""
__version__ = "1.0"

"""Every module of the library, used once, on the capstone problem."""
from dmkit.boolean import minimise, truth_vector
from dmkit.colour import chromatic_number, greedy_colour
from dmkit.combin import combinations_count
from dmkit.counting import product_rule
from dmkit.crypto import mod_pow, totient
from dmkit.graph import Graph, components
from dmkit.logic import equivalent
from dmkit.number import is_prime_trial
from dmkit.prob import probability, sample_space
from dmkit.proof import for_all
from dmkit.recur import iterate
from dmkit.sets import is_function
from dmkit.tree import spanning_tree

wants = {"Ada": ["logic", "sets", "graphs"],
         "Ben": ["sets", "counting", "primes"],
         "Cleo": ["graphs", "trees", "colouring"],
         "Dan": ["logic", "counting", "trees"],
         "Eve": ["primes", "colouring", "graphs"]}
talks = sorted({t for wanted in wants.values() for t in wanted})
clashes = sorted({tuple(sorted((a, b))) for wanted in wants.values()
                  for a in wanted for b in wanted if a < b})
g = Graph(talks, clashes)
colour = greedy_colour(g)
slots = sorted(set(colour.values()))
space = sample_space(slots, repeat=1)

answers = [
    (1, "logic", "the rule written two ways agrees",
     equivalent(lambda c, s: not (c and s), lambda c, s: (not c) or (not s),
     ["c", "s"])),
    (2, "proof", "does every talk have a slot", for_all(lambda t: t in colour, talks)),
    (3, "sets", "is the timetable a function on talks",
     is_function(sorted(colour.items()), talks)),
    (4, "induct", "every attendee has three slots",
     all(len({colour[t] for t in w}) == 3 for w in wants.values())),
    (5, "counting", "assignments of 4 slots to 7 talks",
     product_rule(*[len(slots)] * len(talks))),
    (6, "combin", "ways to pick 3 talks of 7", combinations_count(len(talks), 3)),
    (7, "prob", "chance a random slot holds one talk",
     probability(space, lambda o: o[0] == 1)),
    (8, "recur", "the eighth term of a(n)=a(n-1)+a(n-2)",
    iterate([1, 1], [1, 1], 9)[8]),
    (9, "number", "is the count of clashes prime", is_prime_trial(len(clashes))),
    (10, "crypto", "7 to the totient of 11, modulo 11", mod_pow(7, totient(11), 11)),
    (11, "graph", "pieces the clash graph is in", len(components(g))),
    (12, "tree", "edges in a spanning tree of it", len(spanning_tree(g).edges())),
    (13, "colour", "the fewest slots the clashes allow", chromatic_number(g)),
    (14, "boolean", "terms in the smallest majority rule",
     len(minimise(truth_vector(lambda a, b, c: sum([a, b, c]) >= 2, 3), 3))),
]
print(f"{'day':>5} {'module':>10} {'what it answers here':>40} {'the answer':>22}")
for day, module, question, answer in answers:
    print(f"{day:>5} {module:>10} {question:>40} {str(answer):>22}")

"""The capstone problem, stated and turned into the objects the book has built."""
from dmkit.counting import product_rule
from dmkit.graph import Graph, degrees

# A CONFERENCE WITH SEVEN TALKS AND FIVE ATTENDEES. Each attendee wants to hear some of
# the talks. Two talks clash when somebody wants both. The whole problem is in this
# dictionary.
wants = {"Ada": ["logic", "sets", "graphs"],
         "Ben": ["sets", "counting", "primes"],
         "Cleo": ["graphs", "trees", "colouring"],
         "Dan": ["logic", "counting", "trees"],
         "Eve": ["primes", "colouring", "graphs"]}
talks = sorted({t for wanted in wants.values() for t in wanted})
clashes = sorted({tuple(sorted((a, b))) for wanted in wants.values()
                  for a in wanted for b in wanted if a < b})
clash_graph = Graph(talks, clashes)

print(f"{'attendee':>8} {'wants to hear':>36}")
for who in sorted(wants):
    print(f"{who:>8} {str(sorted(wants[who])):>36}")
print()
print(f"talks: {len(talks)}, clashes: {len(clashes)}")
print(f"{'talk':>10} {'clashes with':>12} {'they are':>44}")
d = degrees(clash_graph)
for talk in talks:
    print(f"{talk:>10} {d[talk]:>12} {str(clash_graph.neighbours(talk)):>44}")
print()
print(f"ways to give each talk one of 4 slots, ignoring clashes: "
      f"{product_rule(*[4] * len(talks))}")

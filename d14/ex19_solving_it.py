"""The capstone problem solved, with a routine from six earlier days."""
from dmkit.colour import chromatic_number, greedy_colour, is_proper, maximum_matching
from dmkit.counting import product_rule
from dmkit.graph import Graph, components, degrees
from dmkit.tree import is_tree, spanning_tree

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
slots = {}
for talk, c in colour.items():
    slots.setdefault(c, []).append(talk)

print(f"DAY 11. {len(g.vertices())} talks, {len(g.edges())} clashes, "
      f"{len(components(g))} piece; the degrees add to {sum(degrees(g).values())}")
print(f"DAY 5.  all assignments of {len(slots)} slots: "
      f"{product_rule(*[len(slots)] * len(talks))}")
print(f"DAY 13. greedy uses {len(set(colour.values()))} slots, the fewest is "
      f"{chromatic_number(g)}, and the timetable is valid: {is_proper(g, colour)}")
for c in sorted(slots):
    print(f"   slot {c}: {sorted(slots[c])}")
tree = spanning_tree(g)
print(f"DAY 12. a spanning tree of the clash graph: {len(tree.edges())} edges, "
      f"a tree: {is_tree(tree)}")
pairs = Graph(sorted(wants) + [f"slot{c}" for c in slots],
              [(who, f"slot{c}") for who in sorted(wants) for c in slots
               if any(colour[t] == c for t in wants[who])])
matching = maximum_matching(pairs)
print(f"DAY 13. attendees paired to slots: {len(matching)} of {len(wants)}")
print(f"DAY 4.  every attendee's three talks land in three different slots: "
      f"{all(len({colour[t] for t in w}) == 3 for w in wants.values())}")

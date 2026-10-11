"""A timetable is a colouring, and the conflicts are the edges."""
from dmkit.colour import chromatic_number, greedy_colour, is_proper
from dmkit.graph import Graph

# SIX EXAMS AND THE STUDENTS TAKING THEM. Two exams clash when some student takes both,
# so the graph has an edge exactly where two exams cannot share a slot.
takes = {"Ada": ["maths", "logic"], "Ben": ["logic", "history"],
         "Cleo": ["maths", "history", "art"], "Dan": ["art", "music"],
         "Eve": ["music", "logic"], "Finn": ["history", "sport"]}
exams = sorted({e for taken in takes.values() for e in taken})
clashes = sorted({tuple(sorted((a, b))) for taken in takes.values()
                  for a in taken for b in taken if a < b})
g = Graph(exams, clashes)
colour = greedy_colour(g)
slots = {}
for exam, c in colour.items():
    slots.setdefault(c, []).append(exam)

print(f"exams: {exams}")
print(f"clashes: {len(clashes)}")
print(f"{'slot':>6} {'exams in it':>34}")
for c in sorted(slots):
    print(f"{c:>6} {str(sorted(slots[c])):>34}")
print()
print(f"a valid timetable: {is_proper(g, colour)}, slots used: {len(slots)}, "
      f"slots needed: {chromatic_number(g)}")
print(f"every student's exams are in different slots: "
      f"{all(len({colour[e] for e in t}) == len(t) for t in takes.values())}")

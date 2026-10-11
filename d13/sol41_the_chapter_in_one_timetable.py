"""Problem 13.28: a timetable, a room allocation and a pairing, from one graph each."""
import networkx as nx

from dmkit.colour import (chromatic_number, greedy_colour, is_bipartite, is_proper,
                          maximum_matching)
from dmkit.graph import Graph, degrees

takes = {"Ada": ["maths", "logic", "art"], "Ben": ["logic", "history"],
         "Cleo": ["maths", "history", "music"], "Dan": ["art", "music", "sport"],
         "Eve": ["music", "logic"], "Finn": ["history", "sport"],
         "Gus": ["maths", "sport"]}
exams = sorted({e for taken in takes.values() for e in taken})
clashes = sorted({tuple(sorted((a, b))) for taken in takes.values()
                  for a in taken for b in taken if a < b})
clash_graph = Graph(exams, clashes)
colour = greedy_colour(clash_graph)
slots = {}
for exam, c in colour.items():
    slots.setdefault(c, []).append(exam)

print(f"exams: {exams}")
print(f"clashes: {len(clashes)}, the degrees {degrees(clash_graph)}")
print(f"slots the greedy walk uses: {len(set(colour.values()))}, "
      f"slots needed: {chromatic_number(clash_graph)}, "
      f"valid: {is_proper(clash_graph, colour)}")
for c in sorted(slots):
    print(f"   slot {c}: {sorted(slots[c])}")
print(f"every student's exams are in different slots: "
      f"{all(len({colour[e] for e in t}) == len(t) for t in takes.values())}")
print()
rooms = {"small": ["maths", "logic", "art"], "medium": ["history", "music"],
         "large": ["sport", "maths", "history"]}
room_graph = Graph(sorted(rooms) + exams,
                   [(r, e) for r, es in rooms.items() for e in es])
matching = maximum_matching(room_graph)
other = nx.Graph()
other.add_nodes_from(room_graph.vertices())
other.add_edges_from(room_graph.edges())
theirs = nx.max_weight_matching(other, maxcardinality=True)
print(f"the room graph is bipartite: {is_bipartite(room_graph)}, "
      f"and NetworkX agrees: {is_bipartite(room_graph) == nx.is_bipartite(other)}")
print(f"the largest pairing of rooms to exams: {matching}")
print(f"   rooms used: {len(matching)} of {len(rooms)}, "
      f"NetworkX finds the same size: {len(matching) == len(theirs)}")

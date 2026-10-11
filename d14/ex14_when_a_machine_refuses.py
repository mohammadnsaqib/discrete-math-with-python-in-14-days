"""A missing move is a refusal, and the machine says so rather than crashing."""
from dmkit.boolean import StateMachine, all_words

# ACCEPTS WORDS THAT START WITH a AND END WITH b. The move table is deliberately
# incomplete: a word that goes wrong falls out of the table and the machine refuses it.
machine = StateMachine(states=["start", "seen_a", "ends_b"], start="start",
                       accepting=["ends_b"],
                       moves={("start", "a"): "seen_a",
                              ("seen_a", "a"): "seen_a", ("seen_a", "b"): "ends_b",
                              ("ends_b", "a"): "seen_a", ("ends_b", "b"): "ends_b"})
missing = [(s, c) for s in machine.states for c in "ab"
           if (s, c) not in machine.moves]
print(f"the move table has {len(machine.moves)} entries for "
      f"{len(machine.states) * 2} state-and-symbol pairs")
print(f"the missing ones: {missing}")
print()
print(f"{'word':>10} {'the states':>34} {'accepted':>10}")
for word in ["", "a", "b", "ab", "ba", "aab", "abab", "abba"]:
    shown = " ".join("-" if s is None else s for s in machine.run(word))
    print(f"{repr(word):>10} {shown:>34} {str(machine.accepts(word)):>10}")
print()
rule = lambda w: len(w) >= 2 and w[0] == "a" and w[-1] == "b"
faults = [w for w in all_words("ab", 8) if machine.accepts(w) != rule(w)]
refused = [w for w in all_words("ab", 4) if None in machine.run(w)]
print(f"words up to length 8 where the machine disagreed with the rule: {len(faults)}")
print(f"words up to length 4 refused outright: {len(refused)}, "
      f"the first few {refused[:5]}")

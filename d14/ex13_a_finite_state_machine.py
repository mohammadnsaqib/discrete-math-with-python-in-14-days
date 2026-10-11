"""A machine with a few states, reading one symbol at a time."""
from dmkit.boolean import StateMachine, all_words

# ACCEPTS WORDS OVER a AND b WITH AN EVEN NUMBER OF a. Two states are enough: one for an
# even count so far and one for an odd count, and each a swaps them.
machine = StateMachine(states=["even", "odd"], start="even", accepting=["even"],
                       moves={("even", "a"): "odd", ("odd", "a"): "even",
                              ("even", "b"): "even", ("odd", "b"): "odd"})
print(f"{'state':>8} {'on a':>8} {'on b':>8}")
for state in machine.states:
    print(f"{state:>8} {machine.moves[(state, 'a')]:>8} "
          f"{machine.moves[(state, 'b')]:>8}")
print()
print(f"{'word':>10} {'the states it passes through':>36} {'accepted':>10} "
      f"{'a count':>9}")
for word in ["", "a", "ab", "aab", "abab", "aaa", "babab"]:
    print(f"{repr(word):>10} {' '.join(machine.run(word)):>36} "
          f"{str(machine.accepts(word)):>10} {word.count('a'):>9}")
print()
words = all_words("ab", 8)
faults = [w for w in words if machine.accepts(w) != (w.count("a") % 2 == 0)]
print(f"words up to length 8 tested: {len(words)}, disagreements: {len(faults)}")

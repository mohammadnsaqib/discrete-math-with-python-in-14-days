"""Arrangements of a word whose letters are not all different."""
from itertools import permutations

from dmkit.combin import distinct_arrangements, factorial_of, multiset_permutations

words = ["abc", "aab", "aaab", "abab", "banana", "letter"]
print(f"{'word':>10} {'letters':>9} {'counts':>16} {'by the rule':>13} "
      f"{'distinct built':>16} {'agree':>7}")
for word in words:
    counts = [word.count(ch) for ch in sorted(set(word))]
    counted = multiset_permutations(counts)
    built = len(distinct_arrangements(word))
    print(f"{word:>10} {len(word):>9} {str(counts):>16} {counted:>13} {built:>16} "
          f"{str(counted == built):>7}")
print()
word = "aab"
everything = ["".join(p) for p in permutations(word)]
print(f"itertools gives {len(everything)} arrangements of '{word}': {everything}")
print(f"distinct ones: {[''.join(p) for p in distinct_arrangements(word)]}")
print(f"{len(word)}! is {factorial_of(len(word))} and 2! is {factorial_of(2)}, "
      f"so {factorial_of(len(word))} over {factorial_of(2)} is "
      f"{factorial_of(len(word)) // factorial_of(2)}")

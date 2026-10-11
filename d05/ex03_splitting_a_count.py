"""Counting a hard collection by splitting it into groups that share nothing."""
from dmkit.counting import enumerate_check, report_count, sum_rule


def three_letter_words(alphabet):
    """Every three-letter string over the alphabet, in a fixed order."""
    return [a + b + c for a in alphabet for b in alphabet for c in alphabet]


letters = list("abcde")
words = three_letter_words(letters)
by_first = {ch: [w for w in words if w[0] == ch] for ch in letters}

print(f"{'first letter':>14} {'how many words':>16}")
for ch in letters:
    print(f"{ch:>14} {len(by_first[ch]):>16}")
print()
print(f"{'collection':>34} {'by the rule':>12} {'by building':>12}  verdict")
print(report_count(enumerate_check(
    sum_rule(*[len(by_first[ch]) for ch in letters]),
    lambda: words,
    "three letters over five")))
print()
overlaps = [(a, b) for a in letters for b in letters
            if a < b and set(by_first[a]) & set(by_first[b])]
print(f"pairs of groups that share a word: {overlaps}")

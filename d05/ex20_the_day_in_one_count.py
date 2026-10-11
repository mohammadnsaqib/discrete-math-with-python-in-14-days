"""Every rule of the day used once, on a count that is then taken past enumeration."""
from itertools import product

from dmkit.counting import (complement_rule, count_functions, enumerate_check,
                            inclusion_exclusion, pigeonhole, report_count, strings_over)

alphabet = list("abcd")
length = 5

total = count_functions(length, len(alphabet))
missing_a = count_functions(length, len(alphabet) - 1)
missing_two = count_functions(length, len(alphabet) - 2)
missing_three = count_functions(length, len(alphabet) - 3)

# EVERY LETTER USED is counted by removing the strings that miss one, putting back those
# that miss two, and so on -- Section 5.4's alternation, applied to a set of strings.
uses_all = (total - 4 * missing_a + 6 * missing_two - 4 * missing_three)

print(f"{'collection':>34} {'by the rule':>12} {'by building':>12}  verdict")
print(report_count(enumerate_check(
    total, lambda: strings_over(alphabet, length), "all strings of length 5")))
print(report_count(enumerate_check(
    complement_rule(total, missing_a),
    lambda: [s for s in strings_over(alphabet, length) if "a" in s],
    "using at least one a")))
print(report_count(enumerate_check(
    uses_all,
    lambda: [s for s in strings_over(alphabet, length)
             if all(ch in s for ch in alphabet)],
    "using every one of the four")))
print()
repeat = pigeonhole(length, len(alphabet))
print(f"a string of length {length} over {len(alphabet)} letters repeats some letter "
      f"at "
      f"least {repeat} times.")
print()
big_length = 30
big = count_functions(big_length, len(alphabet))
print(f"strings of length {big_length} over the same four letters: {big}")

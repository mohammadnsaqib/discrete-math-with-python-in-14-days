"""How the count of strings grows with their length, checked while it can be."""
from dmkit.counting import (count_functions, enumerate_check, report_count,
                            strings_over)

alphabet = list("abcd")
print(f"{'length':>8} {'by the rule':>14} {'by building':>14} {'agree':>8}")
for length in range(0, 8):
    counted = count_functions(length, len(alphabet))
    result = enumerate_check(counted, lambda k=length: strings_over(alphabet, k), "")
    print(f"{length:>8} {counted:>14} {result['built']:>14} {str(result['agree']):>8}")
print()
print(f"the eight strings of length 2 starting with a or b: "
      f"{[s for s in strings_over(alphabet, 2) if s[0] in 'ab']}")
print()
big = count_functions(12, 26)
print(f"strings of length 12 over 26 letters: {big}")
years = big // (1000000 * 60 * 60 * 24 * 365)
print(f"that one was NOT built. Building it at a million strings a second would take "
      f"about")
print(f"{years} years. So the rule is used, and the check is left to the small cases "
      f"above,")
print("where the rule and the collection it sizes agree at every length.")

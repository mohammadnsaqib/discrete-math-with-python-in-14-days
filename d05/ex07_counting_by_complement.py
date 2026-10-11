"""Counting what is left, when the thing itself has too many shapes."""
from dmkit.counting import (complement_rule, count_functions, enumerate_check,
                            report_count, strings_over)

alphabet = list("abc")
length = 4
total = count_functions(length, len(alphabet))
without_a = count_functions(length, len(alphabet) - 1)

print(f"{'strings of length 4 over a, b, c':>34} : {total}")
print(f"{'of those, the ones with no a':>34} : {without_a}")
print()
print(f"{'collection':>34} {'by the rule':>12} {'by building':>12}  verdict")
print(report_count(enumerate_check(
    complement_rule(total, without_a),
    lambda: [s for s in strings_over(alphabet, length) if "a" in s],
    "at least one 'a'")))
print(report_count(enumerate_check(
    without_a,
    lambda: [s for s in strings_over(alphabet, length) if "a" not in s],
    "no 'a' at all")))

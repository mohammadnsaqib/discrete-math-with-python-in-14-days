"""The sum rule, and the collection it claims to size, built and measured."""
from dmkit.counting import enumerate_check, report_count, sum_rule

vowels = ["a", "e", "i", "o", "u"]
digits = [str(d) for d in range(10)]
punctuation = [".", ",", ";"]

print(f"{'collection':>34} {'by the rule':>12} {'by building':>12}  verdict")
print(report_count(enumerate_check(
    sum_rule(len(vowels), len(digits)),
    lambda: vowels + digits,
    "one vowel or one digit")))
print(report_count(enumerate_check(
    sum_rule(len(vowels), len(digits), len(punctuation)),
    lambda: vowels + digits + punctuation,
    "one of three separate groups")))
print(report_count(enumerate_check(
    sum_rule(len(vowels)),
    lambda: vowels,
    "one vowel")))
print(report_count(enumerate_check(
    sum_rule(),
    lambda: [],
    "one of no groups at all")))

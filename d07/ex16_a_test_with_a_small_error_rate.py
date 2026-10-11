"""A test that is right 99 times in 100, on a condition one person in a thousand has."""
from fractions import Fraction

from dmkit.prob import bayes

prior = Fraction(1, 1000)
likelihood = Fraction(99, 100)
false_positive = Fraction(1, 100)

answer = bayes(prior, likelihood, false_positive)
print(f"how common the condition is       : {prior} = {float(prior):.6f}")
print(f"the test says yes when present    : {likelihood} = {float(likelihood):.6f}")
print(f"the test says yes when absent     : {false_positive} = "
      f"{float(false_positive):.6f}")
print()
population = 100000
with_it = population * prior
without_it = population - with_it
true_yes = with_it * likelihood
false_yes = without_it * false_positive
print(f"in a population of {population}:")
print(f"   have the condition            : {int(with_it)}")
print(f"   of those, the test says yes   : {int(true_yes)}")
print(f"   do not have it                : {int(without_it)}")
print(f"   of those, the test says yes   : {int(false_yes)}")
print(f"   all who hear yes              : {int(true_yes + false_yes)}")
print()
print(f"P(has it given the test says yes) = {answer} = {float(answer):.6f}")
print(f"the counts agree: "
      f"{Fraction(int(true_yes), int(true_yes + false_yes)) == answer}")

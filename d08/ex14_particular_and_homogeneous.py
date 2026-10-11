"""Two pieces make a solution: one that answers the added term and one that fits the
start."""
from fractions import Fraction

from dmkit.recur import agrees_with, iterate


def constant_particular(coefficient, added):
    """The constant c satisfying c = coefficient*c + added, when one exists."""
    if coefficient == 1:
        return None
    return Fraction(added, 1 - coefficient)


cases = [
    ("a(n) = 2*a(n-1) + 1", 2, 1, [0]),
    ("a(n) = 3*a(n-1) + 4", 3, 4, [1]),
    ("a(n) = 5*a(n-1) - 8", 5, -8, [3]),
    ("a(n) = 2*a(n-1) + 6", 2, 6, [2]),
]
print(f"{'recurrence':>24} {'particular':>12} {'homogeneous part':>20} "
      f"{'closed form':>26} {'disagreement':>15}")
for text, coefficient, added, initial in cases:
    particular = constant_particular(coefficient, added)
    a = Fraction(initial[0]) - particular
    formula = lambda n, a=a, r=coefficient, p=particular: a * r ** n + p
    terms = iterate([coefficient], initial, 30, lambda n, v=added: v)
    where = agrees_with(formula, terms, tolerance=0)
    label = "none in 0..29" if where is None else f"at n = {where}"
    sign = "+" if particular >= 0 else "-"
    whole = f"{a} * {coefficient}**n {sign} {abs(particular)}"
    print(f"{text:>24} {str(particular):>12} {f'{a} * {coefficient}**n':>20} "
          f"{whole:>26} {label:>15}")
print()
coefficient, added, initial = 2, 1, [0]
particular = constant_particular(coefficient, added)
terms = iterate([coefficient], initial, 11, lambda n: added)
print(f"{'n':>4} {'iterated':>10} {'homogeneous':>13} {'particular':>12} {'sum':>8}")
a = Fraction(initial[0]) - particular
for n in range(6):
    print(f"{n:>4} {terms[n]:>10} {str(a * coefficient ** n):>13} "
          f"{str(particular):>12} {str(a * coefficient ** n + particular):>8}")

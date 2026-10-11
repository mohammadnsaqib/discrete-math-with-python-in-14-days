"""The same claim reached three ways, and the check that all three agree."""
from dmkit.proof import check_over, direct_check, is_even, is_odd, report

dom = range(1, 301)

# CLAIM. For every n, n squared plus n is even.
# DIRECT.        n(n+1) is a product of consecutive integers, one of which is even.
# BY CASES.      n even: n^2 and n are both even, so the sum is. n odd: both are odd,
#                and odd plus odd is even.
# CONTRADICTION. Suppose n^2 + n were odd. Then n(n+1) is odd, so both factors are odd,
#                so n and n+1 are both odd -- impossible for consecutive integers.
print("claim: n squared plus n is even, for every n")
print()
print("  direct        " + report(check_over(lambda n: is_even(n * n + n), dom,
                                             "the integers 1 to 300")))
evens = direct_check(is_even, lambda n: is_even(n * n + n), dom)
odds = direct_check(is_odd, lambda n: is_even(n * n + n), dom)
print(f"  by cases      even n: {evens['tested']} tested, {evens['failures']} failed; "
      f"odd n: {odds['tested']} tested, {odds['failures']} failed")
print("  contradiction " + report(check_over(lambda n: not is_odd(n * n + n), dom,
                                             "the integers 1 to 300")))

"""Problem 2.25: a checker that reports what a search did, never a verdict."""
from dmkit.proof import check_over, is_prime_slow, report


def study(text, predicate, domain, description):
    """Run the search and print the claim beside exactly what the search established."""
    result = check_over(predicate, domain, description)
    print(f"{text}")
    print(f"   {report(result)}")
    if result["refuted"]:
        print(f"   substitute {result['witness']!r} into the claim and it fails")
    else:
        print(f"   the claim is where it was before this ran")
    print()


study("every integer from 2 to 200 is prime", is_prime_slow, range(2, 201),
      "the integers 2 to 200")
study("every integer from 2 to 200 has a prime factor",
      lambda n: any(is_prime_slow(d) and n % d == 0 for d in range(2, n + 1)),
      range(2, 201), "the integers 2 to 200")
study("every multiple of 4 below 400 is a multiple of 2",
      lambda n: n % 2 == 0, range(0, 400, 4), "the multiples of 4 below 400")
study("every integer from 1 to 300 is a sum of three squares",
      lambda n: any(a * a + b * b + c * c == n
                    for a in range(18) for b in range(18) for c in range(18)),
      range(1, 301), "the integers 1 to 300")

"""A statement is a sentence with a truth value. Having one is not the same as knowing
it."""

# (sentence, is it a statement, its value if that is settled)
sentences = [
    ("Seven is prime.", True, True),
    ("Seven is even.", True, False),
    ("Twelve divides sixty.", True, True),
    ("Every even number above two is a sum of two primes.", True, None),
    ("What time is it?", False, None),
    ("Close the door.", False, None),
    ("x is greater than five.", False, None),
]

print(f"{'sentence':>54} {'statement?':>12} {'value':>9}")
for text, is_statement, value in sentences:
    shown = str(value) if value is not None else ("unsettled" if is_statement else "-")
    print(f"{text:>54} {str(is_statement):>12} {shown:>9}")

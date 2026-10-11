"""Three claims read off the triangle, each checked against the numbers themselves."""
from dmkit.combin import binomial, pascal_row

rows = 10
print(f"{'diagonal':>10} {'the first eight entries':>40} {'what they are':>22}")
names = {0: "all ones", 1: "the counting numbers", 2: "the triangular numbers",
         3: "the tetrahedral numbers"}
for d in range(4):
    entries = [binomial(d + i, d) for i in range(8)]
    print(f"{d:>10} {str(entries):>40} {names[d]:>22}")
print()
print(f"{'n':>4} {'k':>4} {'sum down the diagonal':>23} {'binomial(n+1, k+1)':>20} "
      f"{'agree':>7}")
for k in range(0, 4):
    for n in range(k, k + 4):
        running = sum(binomial(i, k) for i in range(k, n + 1))
        print(f"{n:>4} {k:>4} {running:>23} {binomial(n + 1, k + 1):>20} "
              f"{str(running == binomial(n + 1, k + 1)):>7}")
print()
print(f"{'n':>4} {'largest entry':>15} {'where it sits':>15} {'row total':>11} "
      f"{'largest share':>15}")
for n in range(2, 11):
    row = pascal_row(n)
    peak = max(row)
    print(f"{n:>4} {peak:>15} {row.index(peak):>15} {sum(row):>11} "
          f"{peak / sum(row):>15.4f}")

"""Memoisation trades memory for time, and the trade is measurable."""
from dmkit.induct import fib_memo

fib_memo.cache_clear()
print(f"before any call: {fib_memo.cache_info()}")
fib_memo(30)
print(f"after F(30)    : {fib_memo.cache_info()}")
fib_memo(30)
print(f"after F(30) twice: {fib_memo.cache_info()}")
fib_memo(60)
print(f"after F(60)    : {fib_memo.cache_info()}")
print()
info = fib_memo.cache_info()
print(f"{'entries kept':>14} {'hits':>8} {'misses':>8} {'hit rate':>10}")
rate = info.hits / (info.hits + info.misses)
print(f"{info.currsize:>14} {info.hits:>8} {info.misses:>8} {rate:>10.3f}")

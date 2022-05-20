# fib number
# Fn = Fn-1 + Fn-2

def fib(n):
  if n <= 2:
    return 1
  return fib(n-1) + fib(n-2)


=================================
# better for larger numbers
# uses 'memoization' to store values without having to travese duplicate points

def fib(n, memo = {}):
  if n in memo:
    return memo[n]
  if n <= 2:
    return 1
  memo[n] = fib(n-1, memo) + fib(n-2, memo)
  return memo[n]

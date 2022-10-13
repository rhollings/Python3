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

'''
Let's walk through what this algorithm does.
fib(l) -> return 1
fib(2)
fib(l) -> return 1 fib(0) -> return 0 store 1 at memo[2]
fib(3)
fib(2) -> lookup memo[2] -> return 1 fib(l) -> return 1
store 2 at memo[3]
fib(4)
fib(3) -> lookup memo[3] -> return 2 fib(2) -> lookup memo[2] -> return 1 store 3 at memo[4]
fib(S)
fib(4) -> lookup memo[4] -> return 3 fib(3) -> lookup memo[3] -> return 2 store 5 at memo[S]
'''

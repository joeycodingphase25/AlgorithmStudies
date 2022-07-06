# Joeys Memoized Fib Formula, top donw
# O(n) time and space

def fib(n, dict1={0:1, 1:1}):
    if n in dict1:
        return dict1[n]
    dict1[n] = fib(n-1, dict1) + fib(n-2, dict1)
    return dict1[n]

print(fib(50))
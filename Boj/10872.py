import sys


def factorial(n):
    if n:
        return n * factorial(n - 1)
    else:  # n==0
        return 1


N = int(sys.stdin.readline())
print(factorial(N))

import sys


def fibonacci(order):
    if order == 0:
        return 0
    elif order == 1:
        return 1
    else:
        return fibonacci(order - 1) + fibonacci(order - 2)


n = int(sys.stdin.readline())
print(fibonacci(n))

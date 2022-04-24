import sys

T = int(sys.stdin.readline())
nm = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
count, result = 0, 0

for case in nm:
    for b in range(2, case[0]):
        for a in range(1, b):
            if (a ** 2 + b ** 2 + case[1]) % (a * b) == 0:
                count += 1
    print(count)
    count = 0
# python3으로 제출 시 time:  1.0644638538360596

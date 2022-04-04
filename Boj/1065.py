import sys

N = int(sys.stdin.readline())
if N < 100:
    hansoo = N
else:
    hansoo = 99
    for num in range(100, N + 1):
        nums = list(map(int, str(num)))
        if nums[2] + nums[0] == 2 * nums[1]:
            hansoo += 1
print(hansoo)

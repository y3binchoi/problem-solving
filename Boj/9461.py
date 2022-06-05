# 9461. 파도반 수열
import sys

input = sys.stdin.readline
testcase = int(input())
dp = [0] * 101  # index: 0~100
dp[1], dp[2], dp[3] = 1, 1, 1
dp[4], dp[5] = 2, 2
for i in range(6, 101):
    dp[i] = dp[i - 1] + dp[i - 5]
for _ in range(testcase):
    print(dp[int(input())])

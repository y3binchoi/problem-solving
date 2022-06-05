# 2579. 계단 오르기
n = int(input())
stairs = [0]  # [0]은 사용하지 않음
for _ in range(n):
    stairs.append(int(input()))

if n == 1:
    print(stairs[1])
else:
    dp = [0] * (n + 1)
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, n + 1):
        dp[i] = max(stairs[i] + stairs[i - 1] + dp[i - 3],
                    stairs[i] + dp[i - 2])

    print(dp[n])

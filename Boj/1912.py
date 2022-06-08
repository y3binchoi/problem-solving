# 1912. 연속합
#
# 입력:
#     수열의 길이 n
#     n개의 정수로 이루어진 임의의 수열
# 출력:
#     연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 최대합

n = int(input())
dp = list(map(int, input().split()))

for i in range(1, n):
    dp[i] = max(dp[i - 1] + dp[i], dp[i])
print(max(dp))

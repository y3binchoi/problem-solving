# 11053. 가장 긴 증가하는 부분 수열
# 최장 증가 부분 수열
# (LIS : Longest Increasing Subsequence)
# 예:
#     수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
# 입력:
#     수열 A의 크기 N (1 <= N <= 1,000)
#     수열 A[i] (1 <= A[i] <= 1,000)
# 출력:
#     수열 A의 가장 긴 증가하는 부분 수열의 길이

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(i):
        if arr[i] <= arr[j]:  # 앞의 비교 대상 보다 작음
            continue
        dp[i] = max(dp[i], 1 + dp[j])

print(max(dp))
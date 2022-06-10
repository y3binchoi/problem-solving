# 2156. 포도주 시식
#     1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
#     2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
#
# 입력:
#     포도주 잔의 개수 n
#     포도주 잔에 들어있는 포도주의 양
# 출력:
#     최대로 마실 수 있는 포도주의 양

n = int(input())
wine = []
wine.extend(int(input()) for _ in range(n))

dp = [0] * n  # 현재 잔 이하의 모든 잔을 고려한 최대 섭취량
dp[0] = wine[0]
if n > 1:
    dp[1] = wine[0] + wine[1]
if n > 2:
    dp[2] = max(wine[2] + wine[0], wine[2] + wine[1], dp[1])
for i in range(3, n):
    dp[i] = max(
        wine[i] + dp[i - 2],  # 현재 잔 + 두 칸 전
        wine[i] + wine[i - 1] + dp[i - 3],  # 현재 잔 + 한 칸 전 + 세 칸 전
        dp[i - 1]  # 현재 잔을 먹지 않음 + 한 칸 전
    )

print(dp[n - 1])

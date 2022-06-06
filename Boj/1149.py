# 1149. RGB 거리
# 빨강|초록|파랑 중 하나로 집을 칠한다
# 이웃한 집 끼리 색이 같지 않아야 한다
# 입력:
# 집의 수 N
# {빨강|초록|파랑}으로 칠하는 비용
# 출력:
# 모든 집을 칠하는 최소 비용
import sys

input=sys.stdin.readline
N = int(input())
rgb = [list(map(int, input().split())) for _ in range(N)]

# rgb: dp 테이블. n*3. [i번째 집][선택된 집 색깔 0:R 1:G 2:B] 으로 칠했을 때의 최소 비용 누적 저장
for i in range(1, N):  # 0 번쨰는 맨 처음 이니까 누적할 게 없다.1 번째 부터
    rgb[i][0] = min(rgb[i - 1][1], rgb[i - 1][2]) + rgb[i][0]  # 현재:R, 이전:G or B
    rgb[i][1] = min(rgb[i - 1][0], rgb[i - 1][2]) + rgb[i][1]  # 현재:G, 이전:R or B
    rgb[i][2] = min(rgb[i - 1][0], rgb[i - 1][1]) + rgb[i][2]  # 현재:B, 이전:R or G
print(min(rgb[N - 1][0], rgb[N - 1][1], rgb[N - 1][2]))
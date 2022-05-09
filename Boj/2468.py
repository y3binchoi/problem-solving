import sys


def dfs(x, y):
    if 0 <= x < N and 0 <= y < N:
        if area[x][y] > rain and not visited[x][y]:
            visited[x][y] = 1
            for i in range(4):
                dfs(x + dx[i], y + dy[i])
        else:
            return
    else:
        return


sys.setrecursionlimit(1000 * 10)
input = sys.stdin.readline
# 상하좌우
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

N = int(input())
area = []  # 높이 정보 NxN 행렬
height = set()  # 높이 집합
for _ in range(N):
    arr = list(map(int, input().split()))
    area.append(arr)
    height.update(arr)

safe_zone = 1
for rain in height:
    visited = [[0] * N for _ in range(N)]
    count = 0
    for x in range(N):
        for y in range(N):
            if area[x][y] > rain and not visited[x][y]:
                dfs(x, y)
                count += 1
    # print('rain',rain,'count',count)
    if count > safe_zone:
        safe_zone = count
    # else:  # 영역 개수가 줄어들기 시작하면 더 세볼 필요 없이 max
    #     break
print(safe_zone)

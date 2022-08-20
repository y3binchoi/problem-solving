# 4963. 섬의 개수
import sys


sys.setrecursionlimit(10**6)
dd = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]


def dfs(x, y):
    graph[x][y] += land
    for dx, dy in dd:
        nx = dx+x
        ny = dy+y
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if graph[nx][ny] != 1:
            continue
        dfs(nx, ny)


while True:
    input = sys.stdin.readline
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    land = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] != 1:
                continue
            land += 1
            dfs(i, j)
    print(land)

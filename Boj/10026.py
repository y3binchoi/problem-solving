# 10026. 적록색약
import sys


sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
picture = []
for _ in range(N):
    picture.append(input())
# print(*visited, sep='\n')
dd = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def dfs(x, y):
    visited[x][y] += section
    for dx, dy in dd:
        nx = dx+x
        ny = dy+y
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[nx][ny] != 0:
            continue
        if picture[nx][ny] == picture[x][y]:
            dfs(nx, ny)


def dfs_rg(x, y):  # 적록색약
    visited[x][y] += section_rg
    for dx, dy in dd:
        nx = dx+x
        ny = dy+y
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[nx][ny] != 0:
            continue
        if picture[nx][ny] == picture[x][y]:
            dfs_rg(nx, ny)
        elif picture[nx][ny] != 'B' and picture[x][y] != 'B':
            dfs_rg(nx, ny)


section = 0
visited = [list(0 for _ in range(N)) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] != 0:
            continue
        section += 1
        dfs(i, j)
section_rg = 0  # 적록색약
visited = [list(0 for _ in range(N)) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] != 0:
            continue
        section_rg += 1
        dfs_rg(i, j)
print(section, section_rg)

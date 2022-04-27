import sys

sys.setrecursionlimit(10 ** 4)  # 채점 서버 재귀 깊이 수정


def dfs(i, j):
    if 0 <= i < M and 0 <= j < N:
        if field[i][j]:  # 배추
            field[i][j] = 0
            dfs(i - 1, j)  # 상
            dfs(i + 1, j)  # 하
            dfs(i, j - 1)  # 좌
            dfs(i, j + 1)  # 우


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = list([0] * N for _ in range(M))
    for _ in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1
    earthworm = 0
    for i in range(M):
        for j in range(N):
            if field[i][j]:  # 배추
                dfs(i, j)
                earthworm += 1
    print(earthworm)

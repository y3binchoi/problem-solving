import sys
from collections import deque


def dfs(x, y):
    if 0 <= x < N and 0 <= y < N:  # 행렬 index 내
        if apartment[x][y]:  # 1
            apartment[x][y] = 0
            return 1 + dfs(x, y - 1) + dfs(x, y + 1) + dfs(x - 1, y) + dfs(x + 1, y)
        else:
            return 0
    else:
        return 0


def bfs(start_x, start_y):
    diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    deq = deque([(start_x, start_y)])
    apartment[start_x][start_y] = -1
    count = 0
    while deq:
        x, y = deq.popleft()
        count += 1
        for dx, dy in diff:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < N and 0 <= ny < N:
                if apartment[nx][ny] == 1:
                    deq.append((nx, ny))
                    apartment[nx][ny] = -1
    return count


input = sys.stdin.readline
N = int(input())  # NxN apartment complex
apartment = [list(map(int, input().strip())) for _ in range(N)]  # stdin 맨 끝에 \n 떼줘야.
house = []  # 단지내 집의 수

for i in range(N):
    for j in range(N):
        if apartment[i][j] == 1:
            # house.append(dfs(i, j))
            house.append(bfs(i, j))
house.sort()
print(len(house))
print(*house, sep='\n')

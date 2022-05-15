import sys
from collections import deque

# 입력
input = sys.stdin.readline
n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for adj in graph:  # 번호가 낮은 인접 노드부터 큐에 넣도록
    adj.sort()


# 문제 해결
def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        u = queue.popleft()
        print(u, end=' ')
        for i in graph[u]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


visited = [0] * (n + 1)
dfs(start)
print()
visited = [0] * (n + 1)
bfs(start)

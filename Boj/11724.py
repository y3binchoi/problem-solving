# 연결 요소의 개수
import sys


sys.setrecursionlimit(10**6)
# input
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# PS
def dfs(v):
    visited[v] = linked
    for i in graph[v]:
        if visited[i]:
            continue
        dfs(i)


visited = [0 for _ in range(N+1)]
linked = 0
for i in range(1, N+1):
    if visited[i]:
        continue
    linked += 1
    dfs(i)

# output
print(linked)

# 백준 2606. 바이러스
import sys


def dfs(graph, v, visited):
    visited[v] = 1
    for n in graph[v]:
        if not visited[n]:
            dfs(graph, n, visited)


input = sys.stdin.readline
com = int(input())
lines = int(input())
graph = {}
visited = [0] * (com + 1)  # python은 ++ 없다
for _ in range(lines):  # 네트워크 인접리스트
    x, y = map(int, input().split())
    if x not in graph.keys():
        graph[x] = {y}
    else:
        graph[x].add(y)
    if y not in graph.keys():
        graph[y] = {x}
    else:
        graph[y].add(x)
dfs(graph, 1, visited)
print(sum(visited) - 1)  # 1번을 통해서니까 1번컴은 빼고

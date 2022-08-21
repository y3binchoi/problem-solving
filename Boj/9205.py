# 9205. 맥주 마시면서 걸어가기
from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    visited = [False for _ in range(combi+2)]
    q = deque()
    q.extend(graph[0])
    while q:
        v = q.popleft()
        if v == combi+1:
            return 'happy'
        for u in graph[v]:
            if visited[u]:
                continue
            visited[u] = True
            q.append(u)
    return 'sad'


tc = int(input())
for _ in range(tc):
    combi = int(input())
    x_y = [list(map(int, input().split()))
           for _ in range(combi+2)]  # [0]집 [1~combi] 편의점 [-1=combi+1]락페
    graph = [[] for _ in range(combi+2)]
    for i in range(len(x_y)):
        for j in range(len(x_y)):
            if i == j:
                continue
            if abs(x_y[i][0]-x_y[j][0]) + abs(x_y[i][1]-x_y[j][1]) > 1000:  # 맨해튼 거리
                continue
            graph[i].append(j)
    print(bfs())

import sys
from collections import deque

# 입력
input = sys.stdin.readline
# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# 문제 해결
visited = [-1] * (N + 1)
queue = deque([X])
count = 0
visited[X] = count
while queue:
    now = queue.popleft()
    for next_node in graph[now]:
        if visited[next_node] == -1:
            queue.append(next_node)
            count = visited[now] + 1
            visited[next_node] = count  # now 다음으로 방문하는 노드
    if count > K:
        break

# 출력
if count < K:
    print(-1)
for i in range(1, N + 1):
    if visited[i] == K:
        print(i, end='\n')

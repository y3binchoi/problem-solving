# 5014. 스타트링크
from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [0 for _ in range(f+1)]  # 0~f
q = deque()
q.append(s)
visited[s] = 1
while q:  # bfs
    v = q.popleft()
    if v == g:
        print(visited[v]-1)
        exit(0)
    for move in [u, -d]:
        nv = v + move
        if nv < 1 or nv > f:
            continue
        if visited[nv]:
            continue
        q.append(nv)
        visited[nv] = visited[v]+1
print("use the stairs")
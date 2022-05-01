import sys

sys.setrecursionlimit(1000 * 100)
input = sys.stdin.readline


def dfs(v, colour: int):
    visited[v] = colour
    for i in graph[v]:
        if not visited[i]:  # 0 = 방문 이력 없음
            if not dfs(i, -colour):
                return False
        elif visited[i] == visited[v]:  # 현재 정점과 연결된 정점의 그룹이 같으면 더 탐색할 필요 없음
            return False
    return True  # 그 외의 경우


K = int(input())  # test case: K
for _ in range(K):
    V, E = map(int, input().split())  # vertex, edge
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)  # 정점 방문 체크
    isBipartite = True
    for _ in range(E):
        u, v = map(int, input().split())  # 인접한 두 정점
        graph[u].append(v)
        graph[v].append(u)
    for n in range(1, V + 1):  # 정점 1~V
        if not visited[n]:  # 0 = 방문 이력 없음
            isBipartite = dfs(n, 1)  # 연결 안된 곳이라 1로 시작해도 상관 없음
            if not isBipartite:
                break

    print('YES' if isBipartite else 'NO')
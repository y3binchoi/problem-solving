def dfs(v):
    for u in graph[v]:
        if not degree[u]:
            degree[u] = degree[v] + 1  # 몇번째로 방문하는지
            dfs(u)


# 입력
n = int(input())  # 전체 사람 수
p1, p2 = map(int, input().split())  # p1으로부터 p2의 촌수 계산
graph = [[] for _ in range(n + 1)]  # 사람 0~n
m = int(input())  # 부모-자식 관계 수
for _ in range(m):
    x, y = map(int, input().split())  # x: 부모, y: 자식
    graph[x].append(y)
    graph[y].append(x)

# 문제 해결
degree = [0] * (n + 1)
dfs(p1)
print(degree[p2] if degree[p2] > 0 else -1)

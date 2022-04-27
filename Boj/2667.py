def dfs(i, j):
    if 0 <= i < N and 0 <= j < N:  # 행렬 index 내
        if apartment[i][j]:  # 1
            apartment[i][j] = 0
            return 1 + dfs(i, j - 1) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i + 1, j)
        else:
            return 0
    else:
        return 0


N = int(input())  # NxN apartment complex
apartment = [list(map(int, input())) for _ in range(N)]
house = []  # 단지내 집의 수

for i in range(N):
    for j in range(N):
        if apartment[i][j]:  # 1
            count = dfs(i, j)
            house.append(count)
house.sort()
print(len(house))
print(*house, sep='\n')

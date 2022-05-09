class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cells = [0]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cells.append(self.dfs(i, j, grid, m, n))
        return max(cells)

    def dfs(self, x: int, y: int, grid: List[List[int]], m: int, n: int):
        if 0 <= x < m and 0 <= y < n:
            if grid[x][y] == 1:
                grid[x][y] = 0
                return 1 + \
                       self.dfs(x - 1, y, grid, m, n) + \
                       self.dfs(x + 1, y, grid, m, n) + \
                       self.dfs(x, y - 1, grid, m, n) + \
                       self.dfs(x, y + 1, grid, m, n)
            else:
                return 0
        else:
            return 0

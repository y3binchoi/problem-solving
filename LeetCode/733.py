# 733. Flood Fill
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        target = image[sr][sc]

        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n:  # image 인덱스 범위
                if target == newColor:
                    return
                if image[r][c] != target:
                    return
                else:
                    image[r][c] = newColor
                    dfs(r - 1, c)  # 상
                    dfs(r + 1, c)  # 하
                    dfs(r, c - 1)  # 좌
                    dfs(r, c + 1)  # 우
            else:
                return

        dfs(sr, sc)
        return image

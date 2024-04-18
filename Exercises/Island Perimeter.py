from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        p = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j]:
                    if grid[i][j] == 1:
                        if i < len(grid)-1:
                            p += 1 - grid[i + 1][j]
                        else:
                            p += 1
                        if j < len(grid[0])-1:
                            p += 1 - grid[i][j + 1]
                        else:
                            p += 1
                        if i > 0:
                            p += 1 - grid[i - 1][j]
                        else:
                            p += 1
                        if j > 0:
                            p += 1 - grid[i][j - 1]
                        else:
                            p += 1
                    visited[i][j] = True
        return p


sol = Solution()
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(sol.islandPerimeter(grid))

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0 and j > 0:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
                if i > 0 and j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                if i == 0 and j > 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
        return grid[len(grid) - 1][len(grid[0]) - 1]

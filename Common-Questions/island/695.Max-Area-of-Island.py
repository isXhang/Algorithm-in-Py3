class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        roLen, coLen = len(grid), len(grid[0])

        def dfs(grid, i, j):
            if not 0 <= i < roLen or not 0 <= j < coLen or grid[i][j] != 1: return 0
            grid[i][j] = 0
            return 1 + dfs(grid, i-1, j) + dfs(grid, i, j+1) + \
                dfs(grid, i+1, j) + dfs(grid, i, j-1)

        maxArea = 0
        for i in range(roLen):
            for j in range(coLen):
                maxArea = max(maxArea, dfs(grid, i, j))
        return maxArea

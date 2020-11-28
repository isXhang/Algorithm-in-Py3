class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        roLen, coLen = len(grid), len(grid[0])

        def dfs(grid, i, j):
            if not 0 <= i < roLen or not 0 <= j < coLen or grid[i][j] == '0': return
            grid[i][j] = '0'
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i+1, j)
            dfs(grid, i, j-1)
            return

        ans = 0
        for i in range(roLen):
            for j in range(coLen):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    ans += 1
        return ans

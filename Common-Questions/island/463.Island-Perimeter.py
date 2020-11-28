class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if i-1 < 0: res += 1
                    elif grid[i-1][j] == 0: res += 1

                    if j+1 > col-1: res += 1
                    elif grid[i][j+1] == 0: res += 1

                    if i+1 > row-1: res += 1
                    elif grid[i+1][j] == 0: res += 1

                    if j-1 < 0: res += 1
                    elif grid[i][j-1] == 0: res += 1
        return res

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        roLen, coLen = len(grid), len(grid[0])

        def dfs(grid, i, j):
            if not 0 <= i < roLen or not 0 <= j < coLen: return 1
            if grid[i][j] == 0: return 1
            if grid[i][j] != 1: return 0
            grid[i][j] = 2
            return dfs(grid, i-1, j) + dfs(grid, i, j+1) + \
                dfs(grid, i+1, j) + dfs(grid, i, j-1)

        for i in range(roLen):
            for j in range(coLen):
                if grid[i][j] == 1:
                    return dfs(grid, i, j)

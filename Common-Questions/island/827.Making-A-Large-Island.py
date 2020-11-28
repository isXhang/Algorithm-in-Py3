class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        roLen, coLen = len(grid), len(grid[0])
        hashmap = {}

        def dfs(grid, i, j, index):
            if not 0 <= i < roLen or not 0 <= j < coLen or grid[i][j] == 0: return 0
            if grid[i][j] == index: return 0
            grid[i][j] = index
            return 1 + dfs(grid, i-1, j, index) + dfs(grid, i, j+1, index) + \
                dfs(grid, i+1, j, index) + dfs(grid, i, j-1, index)

        index = 1
        maxSingleArea = 0
        for i in range(roLen):
            for j in range(coLen):
                if grid[i][j] == 1:
                    index += 1
                    hashmap[index] = dfs(grid, i, j, index)
                    maxSingleArea = max(maxSingleArea, hashmap[index])

        maxConnectArea = 0
        for i in range(roLen):
            for j in range(coLen):
                if grid[i][j] == 0:
                    tmpArea = 1
                    indices = []
                    if i-1 >= 0: indices.append(grid[i-1][j])
                    if j+1 < coLen: indices.append(grid[i][j+1])
                    if i+1 < roLen: indices.append(grid[i+1][j])
                    if j-1 >= 0: indices.append(grid[i][j-1])
                    indices = list(set(indices))
                    for index in indices:
                        tmpArea += hashmap.get(index, 0)
                    maxConnectArea = max(maxConnectArea, tmpArea)
        return maxConnectArea if maxConnectArea > maxSingleArea else maxSingleArea


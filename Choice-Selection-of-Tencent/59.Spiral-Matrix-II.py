class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0: return []
        matrix = [[0]*n for _ in range(n)]

        l, r, t, d = 0, n-1, 0, n-1
        num, tar = 0, n*n
        while num < tar:
            for i in range(l, r+1):
                num += 1
                matrix[t][i] = num
            t += 1

            for i in range(t, d+1):
                num += 1
                matrix[i][r] = num
            r -= 1

            for i in range(r, l-1, -1):
                num += 1
                matrix[d][i] = num
            d -= 1

            for i in range(d, t-1, -1):
                num += 1
                matrix[i][l] = num
            l += 1

        return matrix

print(Solution().generateMatrix(2))

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res.extend(matrix[0])
            matrix = matrix[1:]
            matrix = list(zip(*matrix))[::-1]

        return res

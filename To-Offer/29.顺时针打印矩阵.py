class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # One-line Solution
        # return list(matrix[0]) + self.spiralOrder(list(zip(*matrix[1:]))[::-1]) if matrix else []
        if not matrix: return []
        res = []
        while matrix:
            res.extend(matrix[0])
            matrix = list(zip(*matrix[1:]))[::-1]
        return res

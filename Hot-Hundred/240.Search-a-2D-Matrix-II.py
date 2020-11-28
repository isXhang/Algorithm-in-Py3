class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False

        row, col = len(matrix), len(matrix[0])
        x, y = row-1, 0

        while x >= 0 and y < col:
            cur = matrix[x][y]
            if target > cur:
                y += 1
            elif target < cur:
                x -= 1
            else:
                return True

        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False

        row, col = len(matrix), len(matrix[0])
        section = []
        for item in matrix:
            if target < item[-1]:
                section = item
                break
            elif target > item[-1]:
                pass
            else:
                return True

        return target in section

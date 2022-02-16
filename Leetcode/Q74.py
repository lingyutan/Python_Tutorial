class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        while row < len(matrix) and matrix[row][0] <= target:
            row += 1
        if target in matrix[row-1]:
            return True
        return False

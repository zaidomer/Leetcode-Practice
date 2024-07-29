# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        #find potential row
        rowS = 0
        rowE = ROWS-1
        potRow = -1
        while rowS<=rowE:
            rowM = rowS + (rowE-rowS)//2
            if matrix[rowM][0] <= target and matrix[rowM][COLS-1] >= target:
                potRow = rowM
                break
            elif matrix[rowM][0] > target:
                rowE = rowM-1
            else:
                rowS = rowM+1

        if potRow==-1:
            return False

        #find potential col
        colS = 0
        colE = COLS-1
        while colS<=colE:
            colM = colS + (colE-colS)//2
            curr = matrix[potRow][colM]

            if curr==target:
                return True
            elif curr<target:
                colS = colM+1
            else:
                colE = colM-1

        return False
            
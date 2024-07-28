# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # ROWS = len(matrix)
        # COLS = len(matrix[0])

        # colSet=set()
        # rowSet=set()

        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if matrix[i][j]==0:
        #             rowSet.add(i)
        #             colSet.add(j)
        
        # #update rows
        # for row in rowSet:
        #     for col in range(COLS):
        #         matrix[row][col] = 0

        # #update cols
        # for col in colSet:
        #     for row in range(ROWS):
        #         matrix[row][col] = 0
            





        ROWS = len(matrix)
        COLS = len(matrix[0])
        zeroFirstRow = False

        #Mark all rows/cols to zero. Use first row/col to do this (and 1 extra var for first row)
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    if i==0:
                        zeroFirstRow=True
                    else:
                        matrix[i][0]=0

        #update rows & cols
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[row][0]==0 or matrix[0][col]==0:
                    matrix[row][col] = 0

        #update first col
        if matrix[0][0]==0:
            for row in range(ROWS):
                matrix[row][0] = 0

        #update first row
        if zeroFirstRow:
            for col in range(COLS):
                matrix[0][col] = 0

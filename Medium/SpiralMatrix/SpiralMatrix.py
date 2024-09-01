# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        topRow = 0
        botRow = ROWS
        leftCol = 0
        rightCol = COLS
        res = []

        while len(res)<ROWS*COLS:
            for i in range(leftCol, rightCol):
                res.append(matrix[topRow][i])
            topRow+=1

            for i in range(topRow, botRow):
                res.append(matrix[i][rightCol-1])
            rightCol-=1

            if not (leftCol<rightCol and topRow<botRow):
                break

            for i in range(rightCol-1, leftCol-1, -1):
                res.append(matrix[botRow-1][i])
            botRow-=1

            for i in range(botRow-1, topRow-1, -1):
                res.append(matrix[i][leftCol])
            leftCol+=1
        return res

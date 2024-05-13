# https://leetcode.com/problems/score-after-flipping-matrix/?envType=daily-question&envId=2024-05-13

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        #flip rows
        for row in range(len(grid)):
            if grid[row][0]==0:
                self.flipRow(grid, row)

        #flip cols
        for col in range(1,len(grid[0])):
            numOnes = 0
            for row in range(len(grid)):
                if grid[row][col]==1:
                    numOnes+=1
            
            if numOnes < len(grid)/2:
                self.flipCol(grid, col)

        #calc num
        finalSum=0
        for row in range(len(grid)):
            finalSum+=self.calcNum(grid,row)
        return finalSum
    
    def flipCol(self, grid: List[List[int]], col: int):
        for i in range(len(grid)):
            grid[i][col] = grid[i][col]^1

    def flipRow(self, grid: List[List[int]], row: int):
        for col in range(len(grid[row])):
            grid[row][col] = grid[row][col]^1
    
    def calcNum(self, grid: List[List[int]], row: int):
        num = 0
        for col in range(len(grid[row])):
            num+=grid[row][col] * 1<<(len(grid[row])-1 - col)

        return num

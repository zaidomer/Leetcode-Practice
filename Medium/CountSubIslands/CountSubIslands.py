# https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS = len(grid1)
        COLS = len(grid1[0])

        def dfs(row, col):
            if row<0 or col<0 or row>=ROWS or col>=COLS or grid2[row][col]!=1:
                return True
            elif grid2[row][col]==1 and grid1[row][col]==0:
                return False

            grid2[row][col]=-1
            down = dfs(row+1,col) 
            up = dfs(row-1,col) 
            right = dfs(row,col+1) 
            left = dfs(row,col-1)
            return up and down and left and right

        result = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid2[i][j]==1 and dfs(i,j):
                    result+=1

        return result

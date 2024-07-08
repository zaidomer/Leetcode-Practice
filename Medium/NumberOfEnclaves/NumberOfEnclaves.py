# https://leetcode.com/problems/number-of-enclaves/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        result = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                length=[0]
                if grid[i][j]==1 and self.explore(grid, i, j, length):
                    result+=length[0]

        return result

    def explore(self, grid: List[List[int]], row:int, col:int, length:List[int]) -> bool:
        if row<0 or col<0 or row>len(grid)-1 or col>len(grid[0])-1:
            return False
        elif grid[row][col]==0:
            return True

        grid[row][col]=0
        length[0]+=1

        up = self.explore(grid, row-1, col, length)
        down = self.explore(grid, row+1, col, length)
        left = self.explore(grid, row, col-1, length)
        right = self.explore(grid, row, col+1, length)

        return up and down and left and right

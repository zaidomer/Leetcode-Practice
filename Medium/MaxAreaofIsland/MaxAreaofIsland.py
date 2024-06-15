# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        largestIsland = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j]==1:
                    largestIsland = max(largestIsland, self.exploreIsland(i,j,grid))

        return largestIsland

    def exploreIsland(self, i: int, j: int, grid: List[List[int]]) -> int:
        if (i<0) or (j<0) or (i>len(grid)-1) or (j>len(grid[0])-1) or (grid[i][j]==0):
            return 0
        else:
            grid[i][j]=0
            return 1 + self.exploreIsland(i-1,j,grid) + self.exploreIsland(i,j-1,grid) + self.exploreIsland(i+1,j,grid) + self.exploreIsland(i,j+1,grid)

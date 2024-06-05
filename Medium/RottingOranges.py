class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        newCount = 0

        while newCount==0 or newCount != count:
            count = newCount
            newCount = self.update(grid, count)
            
        if 1 in grid:
            return -1
        return newCount
        
    def update(grid, count):
        change = False
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                    if grid[i][j] == 2 and i > 0 and grid[i-1][j]==1:
                        grid[i-1][j] = 2
                        change = True
                    if grid[i][j] == 2 and i < len(grid)-1 and grid[i+1][j]==1:
                        grid[i+1][j] = 2
                        change = True
                    if grid[i][j] == 2 and j < len(grid)-1 and grid[i][j-1]==1:
                        grid[i][j-1] = 2
                        change = True
                    if grid[i][j] == 2 and j < len(grid)-1 and grid[i][j+1]==1:
                        grid[i][j+1] = 2
                        change = True

        if change:
            return count+1
        return count
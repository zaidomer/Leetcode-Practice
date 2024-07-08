# https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        result=0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if not visited[i][j] and grid[i][j]==0 and self.explore(grid, visited, i, j):
                    result+=1
        
        return result

    def explore(self, grid: List[List[int]], visited: List[List[bool]], row:int, col:int) -> bool:
        if row>len(grid)-1 or row<0 or col>len(grid[0])-1 or col<0:
            return False
        elif visited[row][col] or grid[row][col]==1:
            return True

        visited[row][col]=True
        down=self.explore(grid, visited, row+1, col)
        right=self.explore(grid, visited, row, col+1)
        left=self.explore(grid, visited, row, col-1)
        up=self.explore(grid, visited, row-1, col)

        return left and right and up and down


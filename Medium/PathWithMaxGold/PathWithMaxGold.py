# https://leetcode.com/problems/path-with-maximum-gold/

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        count = 0

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col]):
                    count = max(count, self.traverse(grid, visited, row, col, 0))

        return count


    def traverse(self, grid: List[List[int]], visited: List[List[bool]], row: int, col:int, previousGold:int) -> int:        
        visited[row][col]=True
        currentMaxGold = previousGold + grid[row][col] 

        if row-1>=0 and grid[row-1][col] and not visited[row-1][col]:
            currentMaxGold = max(self.traverse(grid, visited, row-1, col, previousGold+grid[row][col]), currentMaxGold)
        if row+1<len(grid) and grid[row+1][col] and not visited[row+1][col]:
            currentMaxGold = max(self.traverse(grid, visited, row+1, col, previousGold+grid[row][col]), currentMaxGold)
        if col-1>=0 and grid[row][col-1] and not visited[row][col-1]:
            currentMaxGold = max(self.traverse(grid, visited, row, col-1, previousGold+grid[row][col]), currentMaxGold)
        if col+1<len(grid[0]) and grid[row][col+1] and not visited[row][col+1]:
            currentMaxGold = max(self.traverse(grid, visited, row, col+1, previousGold+grid[row][col]), currentMaxGold)            
        
        visited[row][col]=False
        return currentMaxGold
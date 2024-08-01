# https://leetcode.com/problems/rotting-oranges/

# class Solution(object):
#     def orangesRotting(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         count = 0
#         newCount = 0

#         while newCount==0 or newCount != count:
#             count = newCount
#             newCount = self.update(grid, count)
            
#         if 1 in grid:
#             return -1
#         return newCount
        
#     def update(grid, count):
#         change = False
#         for i in range(0,len(grid)):
#             for j in range(0,len(grid[i])):
#                     if grid[i][j] == 2 and i > 0 and grid[i-1][j]==1:
#                         grid[i-1][j] = 2
#                         change = True
#                     if grid[i][j] == 2 and i < len(grid)-1 and grid[i+1][j]==1:
#                         grid[i+1][j] = 2
#                         change = True
#                     if grid[i][j] == 2 and j < len(grid)-1 and grid[i][j-1]==1:
#                         grid[i][j-1] = 2
#                         change = True
#                     if grid[i][j] == 2 and j < len(grid)-1 and grid[i][j+1]==1:
#                         grid[i][j+1] = 2
#                         change = True

#         if change:
#             return count+1
#         return count








class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        fresh = 0
        mins = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1

        while q and fresh>0:
            for i in range(len(q)):
                row,col = q.popleft()
                for dr, dc in directions:
                    r = row+dr
                    c = col+dc
                    if r<ROWS and r>=0 and c<COLS and c>=0 and grid[r][c]==1:
                        q.append((r, c))
                        grid[r][c]=2
                        fresh-=1
            mins+=1

        return mins if fresh==0 else -1

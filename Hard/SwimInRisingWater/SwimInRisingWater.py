# https://leetcode.com/problems/swim-in-rising-water/

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        heap = []
        heappush(heap, (grid[0][0],0,0))
        visit = set()

        while heap:
            currMax,row,col = heappop(heap)
            if (row,col) in visit:
                continue
            elif row==ROWS-1 and col==COLS-1:
                return currMax
            visit.add((row,col))
            for dr, dc in directions:
                r = row+dr
                c = col+dc
                if r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in visit:
                    continue
                newMax = max(currMax, grid[r][c])
                heappush(heap, (newMax,r,c))

        return -1

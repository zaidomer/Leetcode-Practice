# https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1

        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        q = deque([(0,0)])
        res=0

        while q:
            res+=1
            for i in range(len(q)):
                row,col = q.popleft()
                if row==ROWS-1 and col==COLS-1:
                    return res
                for dr,dc in directions:
                    r=row+dr
                    c=col+dc
                    if r>=0 and c>=0 and r<ROWS and c<COLS and grid[r][c]==0:
                        grid[r][c]=1
                        q.append((r,c))
        return -1

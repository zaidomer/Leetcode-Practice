# https://leetcode.com/problems/as-far-from-land-as-possible/

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ROWS=len(grid)
        COLS=ROWS
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        res=0

        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    q.append((i,j))
                    grid[i][j]=-1

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr,dc in directions:
                    r=row+dr
                    c=col+dc
                    if r>=0 and c>=0 and r<ROWS and c<COLS and grid[r][c]==0:
                        q.append((r, c))
                        grid[r][c]=-1
            res+=1
        
        return -1 if res==1 else res-1
        
# https://leetcode.com/problems/walls-and-gates/description/
# https://neetcode.io/problems/islands-and-treasure

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = (1<<31)-1
        ROWS = len(grid)
        COLS = len(grid[0])

        count = 1
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    q.append((i,j))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            for i in range(len(q)):
                row,col = q.popleft()
                for dr,dc in directions:
                    r = row+dr
                    c = col+dc
                    if r>=0 and c>=0 and r<ROWS and c<COLS and grid[r][c]==INF:
                        grid[r][c]=count
                        q.append((r,c))
            count+=1

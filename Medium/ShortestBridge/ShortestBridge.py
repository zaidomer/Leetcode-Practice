# https://leetcode.com/problems/shortest-bridge/

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        islandA = deque()

        def dfs(row,col):
            if row<0 or col<0 or row>=ROWS or col>=COLS or grid[row][col]!=1:
                return
            grid[row][col]=-1
            islandA.append((row,col))
            for dr,dc in directions:
                dfs(row+dr,col+dc)

        def bfs():
            res = 0
            while islandA:
                for i in range(len(islandA)):
                    row,col = islandA.popleft()
                    for dr,dc in directions:
                        r=row+dr
                        c=col+dc
                        if r>=0 and c>=0 and r<ROWS and c<COLS:
                            if grid[r][c]==1:
                                return res
                            elif grid[r][c]==0:
                                islandA.append((r,c))
                                grid[r][c]=-1
                res+=1
            return res

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    dfs(i,j)
                    return bfs()
                    
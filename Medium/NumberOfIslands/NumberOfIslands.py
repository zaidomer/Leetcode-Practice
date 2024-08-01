# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ## VALID BFS APPROACH
        # ROWS = len(grid)
        # COLS = len(grid[0])
        
        # result = 0

        # def bfs(row:int, col:int):
        #     q = deque([(row,col)])
        #     while q:
        #         for i in range(len(q)):
        #             row,col = q.popleft()
        #             if grid[row][col]=="1":
        #                 grid[row][col]="0"
        #                 if row+1<ROWS:
        #                     q.append((row+1, col))
        #                 if row-1>=0:
        #                     q.append((row-1, col))
        #                 if col+1<COLS:
        #                     q.append((row, col+1))
        #                 if col-1>=0:
        #                     q.append((row, col-1))


        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if grid[i][j]=="1":
        #             result+=1
        #             bfs(i,j)
        
        # return result











        ## VALID DFS APPROACH
        ROWS = len(grid)
        COLS = len(grid[0])
        
        result = 0

        def dfs(row:int, col:int):
            if row<0 or col<0 or row>=ROWS or col>=COLS or grid[row][col]=="0":
                return

            grid[row][col]="0"
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=="1":
                    result+=1
                    dfs(i, j)
        
        return result

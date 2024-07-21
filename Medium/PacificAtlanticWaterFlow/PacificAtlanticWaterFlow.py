# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # ROWS = len(heights)
        # COLS = len(heights[0])

        # connected = set()
        # result = []

        # def dfs(row:int, col:int, borderResults:List[bool], prev:int, visited:Set[Tuple[int, int]]) -> None:
        #     if (row<0) or (col<0) or (row>=ROWS) or (col>=COLS) or ((row,col) in visited) or (heights[row][col] > prev):
        #         return False

        #     curr = heights[row][col]

        #     if row==ROWS-1 or col==COLS-1:
        #         #Atlantic
        #         borderResults[0]=True
        #     if row==0 or col==0:
        #         #Pacific
        #         borderResults[1]=True

        #     visited.add((row,col))

        #     if (borderResults[0] and borderResults[1]) or ((row,col) in connected):
        #         return True

        #     down = dfs(row+1, col, borderResults, curr, visited)
        #     up = dfs(row-1, col, borderResults, curr, visited)
        #     right = dfs(row, col+1, borderResults, curr, visited)
        #     left = dfs(row, col-1, borderResults, curr, visited)

        #     return down or up or right or left


        # for row in range(ROWS):
        #     for col in range(COLS):
        #         borderResults=[False, False]
        #         visited = set()
        #         if dfs(row, col, borderResults, heights[row][col], visited):
        #             result.append([row, col])
        #             connected.add((row,col))
        
        # return result

        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()

        result = []

        def dfs(row:int, col:int, prev:int, visit:Set[Tuple[int, int]]):
            if (row<0) or (col<0) or (row>=ROWS) or (col>=COLS) or ((row,col) in visit) or (heights[row][col]<prev):
                return
            
            curr = heights[row][col]
            visit.add((row, col))

            dfs(row+1, col, curr, visit)
            dfs(row-1, col, curr, visit)
            dfs(row, col+1, curr, visit)
            dfs(row, col-1, curr, visit)

        for col in range(COLS):
            dfs(0, col, heights[0][col], pacific)
            dfs(ROWS-1, col, heights[ROWS-1][col], atlantic)

        for row in range(ROWS):
            dfs(row, 0, heights[row][0], pacific)
            dfs(row, COLS-1, heights[row][COLS-1], atlantic)

        for coordinates in atlantic:
            if coordinates in pacific:
                result.append(coordinates)

        return result


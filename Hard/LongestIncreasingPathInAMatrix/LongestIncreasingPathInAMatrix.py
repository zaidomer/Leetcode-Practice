class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # VALID INITIAL SOLUTION BUT NOT CONVENTIONAL DFS
        # ROWS = len(matrix)
        # COLS = len(matrix[0])
        # directions = [(1,0), (0,1), (-1,0), (0,-1)]

        # res = 0
        # cache = defaultdict(int)

        # def dfs(row, col):
        #     if (row,col) in cache:
        #         return cache[(row,col)]
        #     cache[(row,col)] = 0
        #     for dr,dc in directions:
        #         r = row+dr
        #         c = col+dc
        #         if r<0 or c<0 or r>=ROWS or c>=COLS or matrix[r][c]<=matrix[row][col]:
        #             continue
        #         cache[(row,col)] = max(cache[(row,col)] , dfs(r,c))
        #     cache[(row,col)]+=1
        #     return cache[(row,col)]

        # for i in range(ROWS):
        #     for j in range(COLS):
        #         res = max(res, dfs(i,j))
        # return res
    










        ROWS = len(matrix)
        COLS = len(matrix[0])

        res = 0
        cache = {}

        def dfs(row, col, prev):
            if row<0 or col<0 or row>=ROWS or col>=COLS or matrix[row][col]<=prev:
                return 0
            elif (row,col) in cache:
                return cache[(row,col)]

            path = 1
            path = max(path, 1+dfs(row+1,col,matrix[row][col]))
            path = max(path, 1+dfs(row-1,col,matrix[row][col]))
            path = max(path, 1+dfs(row,col+1,matrix[row][col]))
            path = max(path, 1+dfs(row,col-1,matrix[row][col]))

            cache[(row,col)]=path
            return cache[(row,col)]

        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dfs(i,j,float("-inf")))
        return res

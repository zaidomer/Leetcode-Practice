# https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # ROWS = len(matrix)
        # COLS = len(matrix[0])
        # directions = [(1,0),(0,1),(1,1)]
        # res = 0

        # def bfs(row, col):
        #     q = deque([(row,col)])
        #     visit = set()
        #     size = 1
            
        #     while q:
        #         for i in range(len(q)):
        #             row,col = q.popleft()
        #             for dr,dc in directions:
        #                 r=row+dr
        #                 c=col+dc
        #                 if r>=ROWS or c>=COLS or matrix[r][c]=='0':
        #                     return size*size
        #                 if (r,c) not in visit:
        #                     q.append((r,c))
        #                     visit.add((r,c))
        #         size+=1
        #     return size*size

        # for row in range(ROWS):
        #     for col in range(COLS):
        #         if matrix[row][col]=='1':
        #             res = max(res, bfs(row,col))
        # return res















        # ROWS = len(matrix)
        # COLS = len(matrix[0])
        # res = 0
        # cache = {}

        # def helper(row,col):
        #     nonlocal res
        #     if row>=ROWS or col>=COLS:
        #         return 0
        #     elif (row,col) not in cache:
        #         right = helper(row,col+1)
        #         down = helper(row+1,col)
        #         diag = helper(row+1,col+1)
        #         cache[(row,col)] = 0

        #         if matrix[row][col]=='1':
        #             cache[(row,col)] = 1+min(right,down,diag)

        #     res = max(res, cache[(row,col)])
        #     return cache[(row,col)]

        # helper(0,0)
        # return res*res















        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        res = 0

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j]=='1':
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    res = max(res, dp[i][j])
        return res*res
        
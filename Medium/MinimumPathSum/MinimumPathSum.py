# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        dp = [[float("inf") for _ in range(COLS+1)] for _ in range(ROWS + 1)]
        dp[-1][-2]=0

        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])

        return dp[0][0]
        
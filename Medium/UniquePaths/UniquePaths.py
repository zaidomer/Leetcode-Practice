# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[m-1][n-1] = 1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i!=m-1 or j!=n-1:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]

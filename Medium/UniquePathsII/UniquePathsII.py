# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] or obstacleGrid[0][0]==1:
            return 0

        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        prevDp = [0 for _ in range(COLS)]
        dp = prevDp[:]
        dp[-1]=1

        for i in range(ROWS-1,-1,-1):
            for j in range(COLS-1,-1,-1):
                if i!=ROWS-1 or j!=COLS-1:
                    down = prevDp[j] if i+1<ROWS and obstacleGrid[i+1][j]==0 else 0
                    right = dp[j+1] if j+1<COLS and obstacleGrid[i][j+1]==0 else 0
                    dp[j] = down+right
            prevDp=dp
            dp = [0 for _ in range(COLS)]
        
        return prevDp[0]

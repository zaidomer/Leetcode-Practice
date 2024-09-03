# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        ##VALID RECURSIVE MEMOIZATION, Time: O(nkt) Space: O(nt) where t=target
        # dp = defaultdict(int)
        # MOD = 10**9+7

        # def dfs(val, dice):
        #     if val==0 and dice==0:
        #         return 1
        #     elif val<0 or dice==0:
        #         return 0
        #     elif (val, dice) in dp:
        #         return dp[(val, dice)]

        #     res = 0
        #     for i in range(1, k+1):
        #         res = (res + dfs(val-i, dice-1))%MOD
        #     dp[(val, dice)] = res
        #     return res

        # return dfs(target, n)









        #VALID BOTTOM UP DP, Time:O(nkt) Space:O(n)
        dp = [0 for _ in range(target)+1]
        dp[0]=1
        MOD = 10**9+7

        for dice in range(n):
            nextDp = [0 for _ in range(target+1)]
            for val in range(1, k+1):
                for total in range(val, target+1):
                    nextDp[total] = (nextDp[total] + dp[total-val])%MOD
            dp = nextDp
        return dp[target]

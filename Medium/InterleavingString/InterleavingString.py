# https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # if len(s1)+len(s2)!=len(s3):
        #     return False

        # dp = {}
        # def dfs(i1, i2, curr):
        #     if (i1,i2) in dp:
        #         return dp[(i1,i2)]
        #     elif curr==s3:
        #         return True
        #     elif len(curr)>0 and curr[-1]!=s3[len(curr)-1]:
        #         return False
            
        #     takeS1 = dfs(i1+1,i2,curr+s1[i1]) if i1<len(s1) else False
        #     takeS2 = dfs(i1,i2+1,curr+s2[i2]) if i2<len(s2) else False
        #     dp[(i1,i2)] = takeS1 or takeS2
        #     return dp[(i1,i2)]

        # return dfs(0,0,"")












        if len(s1)+len(s2)!=len(s3):
            return False
        dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        dp[-1][-1] = True
        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                if i<len(s1) and s1[i]==s3[i+j] and dp[i+1][j]:
                    dp[i][j]=True
                elif j<len(s2) and s2[j]==s3[i+j] and dp[i][j+1]:
                    dp[i][j]=True
        return dp[0][0]

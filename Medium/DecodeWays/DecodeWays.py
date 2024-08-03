# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        # dp = [0 for _ in range(len(s)+1)]
        # dp[-1] = 1
        # digits={'0','1','2','3','4','5','6'}

        # for i in range(len(s)-1, -1, -1):
        #     if s[i]=="0":
        #         dp[i]=0
        #     else:
        #         dp[i]=dp[i+1]

        #     if (i+1)<len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1] in digits)):
        #         dp[i] += dp[i+2]

        # return dp[0]




        dp = {len(s):1}
        def computeStrings(i:int) -> int:
            if i in dp:
                return dp[i]
            elif s[i]=="0":
                return 0

            result = computeStrings(i+1)
            if (i+1)<len(s) and int(s[i:i+2])<=26:
                result += computeStrings(i+2)
            dp[i] = result
            return result

        return computeStrings(0)

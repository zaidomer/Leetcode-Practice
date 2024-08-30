# https://leetcode.com/problems/ones-and-zeroes/

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #VALID RECURSIVE MEMOIZATION
        # dp = {}

        # counts = [[0,0] for _ in range(len(strs))]
        # for i in range(len(strs)):
        #     for j in range(len(strs[i])):
        #         if strs[i][j]=='0':
        #             counts[i][0]+=1
        #         else:
        #             counts[i][1]+=1
        
        # def dfs(i, zeroes, ones):
        #     if i==len(counts):
        #         return 0
        #     elif (i,zeroes,ones) in dp:
        #         return dp[(i,zeroes,ones)]

        #     res = 0
        #     newZeroes = zeroes-counts[i][0]
        #     newOnes = ones-counts[i][1]
        #     if newZeroes>=0 and newOnes>=0:
        #         res = 1 + dfs(i+1, newZeroes, newOnes)
        #     res = max(res, dfs(i+1, zeroes, ones))
        #     dp[(i,zeroes,ones)] = res
        #     return res

        # return dfs(0,m,n)






        #DP Bottom Up
        dp = defaultdict(int)
        for s in strs:
            mCnt = s.count("0")
            nCnt = s.count("1")
            for i in range(m, mCnt-1, -1):
                for j in range(n, nCnt-1, -1):
                    dp[(i,j)] = max(dp[(i,j)], 1+dp[(i-mCnt,j-nCnt)])
        return dp[(m,n)]

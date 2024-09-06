# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

class Solution:
    def maximumLength(self, s: str) -> int:
        right = 0
        res = -1
        count = defaultdict(int)

        while right < len(s):
            i = right
            currLen = 0
            while i<len(s) and s[i]==s[right]:
                currLen+=1
                i+=1
            
            for j in range(1, currLen+1):
                count[(s[right], j)] += currLen-j+1
                if count[(s[right], j)] >= 3:
                    res = max(res, j)
            right = i

        return res

# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        
        def expand(l:int, r:int) -> int:
            res=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            return res

        for i in range(len(s)):
            result += expand(i,i)
            result += expand(i,i+1)
        
        return result

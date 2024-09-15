# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pairs = 0
        res = []
        for ch in s:
            if ch==')':
                if pairs>0:
                    res.append(ch)
                    pairs-=1
            else:
                if ch=='(':
                    pairs+=1
                res.append(ch)
        
        i=len(res)-1
        while i>=0 and pairs>0:
            if res[i]=='(':
                res[i]=''
                pairs-=1
            i-=1
        return ''.join(res)

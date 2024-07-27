# https://leetcode.com/problems/assign-cookies/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        g.sort()
        s.sort()

        gIndex = len(g)-1
        sIndex = len(s)-1

        while sIndex>=0 and gIndex>=0:
            if s[sIndex]>=g[gIndex]:
                result+=1
                sIndex-=1
            gIndex-=1

        return result

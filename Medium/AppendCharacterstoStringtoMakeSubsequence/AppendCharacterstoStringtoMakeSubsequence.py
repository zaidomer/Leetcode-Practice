# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution(object):
    def appendCharacters(self, s, t):
        sIndex, tIndex = 0, 0
    
        while sIndex < len(s) and tIndex < len(t):
            if s[sIndex] == t[tIndex]:
                tIndex += 1
            sIndex += 1
    
        return len(t) - tIndex

        
        
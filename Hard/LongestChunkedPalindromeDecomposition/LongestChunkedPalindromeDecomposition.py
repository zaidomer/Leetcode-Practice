# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/description/

class Solution:
    def longestDecomposition(self, text: str) -> int:
        left = 1
        leftStart=0

        right=len(text)-1
        rightEnd = len(text)
        
        res = 0

        while left<=right:
            if text[leftStart:left]==text[right:rightEnd]:
                res+=2
                leftStart = left
                rightEnd = right
            left+=1
            right-=1

        return res + (1 if rightEnd-leftStart>=1 else 0)   
        
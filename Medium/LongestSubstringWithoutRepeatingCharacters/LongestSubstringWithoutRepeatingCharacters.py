# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #abcxbuiop
        left = 0
        result = 0
        letterDict = {}
        
        for right in range(0, len(s)):
            if letterDict.get(s[right],-1)>=left:
                left = letterDict[s[right]]+1

            letterDict[s[right]] = right
            result = max(result, (right-left+1))

        return result

# https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        res = 0
        vowels = ['a','e','i','o','u']
        windowSize = 0
        j = 0

        for ch in word:
            if j>=0 and ch==vowels[j]:
                windowSize+=1
            elif -1<j<4 and windowSize>0 and ch==vowels[j+1]:
                windowSize+=1
                j+=1
            else:
                if j==4 and windowSize>res:
                    res = windowSize
                windowSize = 0
                if ch=='a':
                    windowSize+=1
                    j=0
                else:
                    j=-1

        if j==4 and windowSize>res:
            res = windowSize
        return res
        
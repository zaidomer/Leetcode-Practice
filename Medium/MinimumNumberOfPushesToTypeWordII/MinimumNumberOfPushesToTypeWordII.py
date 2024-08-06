# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = [0 for _ in range(26)]
        for ch in word:
            counts[ord(ch)-ord('a')]+=1

        counts.sort(reverse=True)
        res=0
        pushes = 1

        for i in range(len(counts)):
            res+=pushes*counts[i]
            if (i+1)%8==0:
                pushes+=1
        return res

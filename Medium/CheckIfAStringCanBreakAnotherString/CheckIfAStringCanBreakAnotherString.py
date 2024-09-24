# https://leetcode.com/problems/check-if-a-string-can-break-another-string/

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = ''.join(sorted(s1))
        s2 = ''.join(sorted(s2))

        larger = max(s1,s2)
        smaller = min(s1,s2)

        for i in range(len(s1)):
            if larger[i]<smaller[i]:
                return False

        return True

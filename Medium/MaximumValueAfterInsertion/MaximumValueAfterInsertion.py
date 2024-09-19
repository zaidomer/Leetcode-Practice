# https://leetcode.com/problems/maximum-value-after-insertion/

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        #Time: O(n), Space: O(n)
        if n[0]!='-':
            for i in range(len(n)):
                if x>int(n[i]):
                    return n[0:i]+str(x)+n[i:]
            return n+str(x)
        else:
            for i in range(1, len(n)):
                if x<int(n[i]):
                    return n[0:i]+str(x)+n[i:]
            return n+str(x)

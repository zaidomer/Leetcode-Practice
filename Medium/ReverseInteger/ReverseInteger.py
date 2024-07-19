# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        mult=1
        if x<0:
            mult=-1
        x = abs(x)

        maxVal = (1<<31)-1
        minVal = 1<<31

        while x>0:
            if (maxVal//10 < result) or (mult<0 and (result > minVal//10)):
                return 0

            result*=10
            result+=x%10
            x=x//10

        result = mult*result
        return result

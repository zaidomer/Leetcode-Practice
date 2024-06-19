# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == -1:
            return 1/x
        elif n == 1:
            return x

        return self.myPow(x*x, n//2) * self.myPow(x, n%2)
# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x

        result = 1
        left = 2
        right = x

        while left<=right:
            mid = left+(right-left)//2
            squared = mid*mid
            if squared<x:
                result = mid
                left = mid+1
            elif squared>x:
                right = mid-1
            else:
                return mid
        
        return result
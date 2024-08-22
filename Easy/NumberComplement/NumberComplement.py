# https://leetcode.com/problems/number-complement/?

class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        i=0
        while num>0:
            res += ((num&1)^1)<<i
            i+=1
            num = num>>1

        return res

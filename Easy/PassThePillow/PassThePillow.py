# https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        diff = time%(n-1)
        if (time//(n-1))%2==1:
            return n-diff
        else:
            return diff+1
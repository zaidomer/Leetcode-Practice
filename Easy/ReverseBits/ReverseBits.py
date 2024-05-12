# https://leetcode.com/problems/reverse-bits/description/

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            nextBit = n & 1
            result = result << 1
            result = result | nextBit
            n = n >> 1
        return result
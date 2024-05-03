# https://leetcode.com/problems/counting-bits/description/

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        rangeSize = 2
        for i in range(0,n+1):
            if i < 2:
                result.append(i)
            else:
                if i==rangeSize*2:
                    rangeSize*=2
                result.append(result[i-rangeSize]+1)

        return result

        
        # 0                    0
        # 1                    1

        # 10                   1
        # 11                   2

        # 100                  1
        # 101                  2
        # 110                  2
        # 111                  3

        # 1000                 1
        # 1001                 2
        # 1010                 2
        # 1011                 3
        # 1100                 2
        # 1101                 3
        # 1110                 3
        # 1111                 4

        # 10000                1
        # 10001                2
        # 10010                2
        # 10011                3

        # 10100                2
        # 10101                3
        # 10110                3
        # 10111                4
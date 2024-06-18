# https://leetcode.com/problems/sum-of-square-numbers

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # if c<=1:
        #     return True

        # for i in range(1, c):
        #     if c-i**2<0:
        #         return False
        #     elif math.sqrt(c-i**2)%1==0:
        #         return True
        
        # return False

        a=0
        b=int(math.sqrt(c))

        while a<=b:
            mid = a*a + b*b
            if mid ==c:
                return True
            elif mid<c:
                a+=1
            else:
                b-=1

        return False
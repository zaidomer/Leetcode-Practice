# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        # cycle=set()
        # while n!=1:
        #     curr = 0
        #     while n>0:
        #         curr+=(n%10)**2
        #         n=n//10
            
        #     if curr in cycle:
        #         return False
                
        #     n=curr
        #     cycle.add(curr)
        
        # return True


        def calc(num: int) -> int:
            res = 0
            while num>0:
                res += (num%10)**2
                num=num//10
            return res
        
        slow = n
        fast = calc(calc(n))

        while slow!=fast:
            slow = calc(slow)
            fast = calc(calc(fast))

        return fast==1
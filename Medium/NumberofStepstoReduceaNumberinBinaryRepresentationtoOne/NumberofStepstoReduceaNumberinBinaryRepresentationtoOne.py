# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

class Solution:
    def numSteps(self, s: str) -> int:
        num=0

        for i in range(0, len(s)):
            num+=int(s[i])*2**(len(s)-1-i)

        steps=0
        while num!=1:
            if num%2==0:
                num=num//2
            else:
                num=num+1
            steps+=1

        return steps
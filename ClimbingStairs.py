#https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # numOnes = n
        # numTwos = 0
        # numSolutions = 1
        # while(numOnes > 1):
        #     numOnes = numOnes - 2
        #     numTwos = numTwos + 1
        #     if numOnes is not 0:
        #         numSolutions = numSolutions + math.factorial(numOnes+numTwos)/(math.factorial(numOnes) * math.factorial(numTwos))
        #     else:
        #         numSolutions = numSolutions+1

        # return numSolutions
        return self.helper(n, {})

    def helper(self, n, data):
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 2

        
        if n in data:
            return data[n]

        data[n] = self.helper(n-1, data) + self.helper(n-2, data)
        return data[n]
        
# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        numSet = set(nums)

        for num in nums:
            newNum = 0
            while num>0:
                newNum = newNum*10 + num%10
                num = num//10
            numSet.add(newNum)

        return len(numSet)

# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)

        return max(self.calc(nums, 0, len(nums)-1), self.calc(nums, 1, len(nums)))

    def calc(self, nums: List[int], start:int, end:int) -> int:
        secondLast = 0
        last = 0

        for i in range(start, end):
            temp = max(nums[i]+secondLast, last)
            secondLast = last
            last = temp

        return last

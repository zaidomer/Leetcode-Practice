# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)

        robSecondLast = nums[0]
        robLast = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = max(robSecondLast+nums[i], robLast)
            robSecondLast = robLast
            robLast = temp

        return robLast

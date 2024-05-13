# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        result = 0
        for i in range(1, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
            elif nums[i-1] > nums[i] < nums[i+1] or nums[i-1] < nums[i] > nums[i+1]:
                result += 1
        return result


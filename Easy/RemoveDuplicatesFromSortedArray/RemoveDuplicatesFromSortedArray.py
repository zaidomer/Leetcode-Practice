# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        replaceIndex = 1
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                nums[replaceIndex]=nums[i]
                replaceIndex+=1

        return replaceIndex

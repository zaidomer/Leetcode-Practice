# https://leetcode.com/problems/sort-colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        map={}

        for i in range(0, len(nums)):
            map[nums[i]] = map.get(nums[i], 0)+1

        count = 0
        for i in range(0,3):
            while map.get(i, -1) > 0:
                nums[count] = i
                map[i]-=1
                count+=1
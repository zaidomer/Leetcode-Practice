#https://leetcode.com/problems/binary-search/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start = 0
        end = len(nums)-1

        while start<=end:
            index = (start+end)//2
            if nums[index] == target:
                print(index)
                return index
            elif nums[index] < target:
                start = index+1
            elif nums[index] > target:
                end = index-1
            
        return -1
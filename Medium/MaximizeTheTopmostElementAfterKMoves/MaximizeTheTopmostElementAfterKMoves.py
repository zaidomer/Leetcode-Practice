# https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums)==1 and k%2==1:
            return -1
        elif k<=1:
            return nums[k]
        elif k<len(nums):
            return max(nums[k], max(nums[0:k-1]))
        elif k==len(nums):
            return max(nums[0:k-1])
        else:
            return max(nums)

# https://leetcode.com/problems/sum-of-beauty-in-the-array/

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        #Time: O(n), Space: O(n)
        right = [float("inf") for _ in range(len(nums))]
        left = [float("-inf") for _ in range(len(nums))]

        for i in range(len(nums)-2,-1,-1):
            right[i] = min(nums[i+1], right[i+1])

        for i in range(1, len(nums)):
            left[i] = max(nums[i-1], left[i-1])

        score = 0
        for i in range(1, len(nums)-1):
            if nums[i]>left[i] and nums[i]<right[i]:
                score+=2
            elif nums[i]>nums[i-1] and nums[i]<nums[i+1]:
                score+=1
        return score

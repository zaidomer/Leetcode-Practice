# https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1 for _ in range(len(nums))]
        stack = deque()

        for j in range(0, len(nums)*2):
            i = j%len(nums)
            while stack and nums[i]>nums[stack[-1]]:
                greaterIndex = stack.pop()
                res[greaterIndex] = nums[i]
            stack.append(i)
        
        return res
        
# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixSum = []

        currSum = 0
        for i in range(len(nums)):
            currSum+=nums[i]
            self.prefixSum.append(currSum)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right]-(self.prefixSum[left-1] if left>0 else 0)     


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

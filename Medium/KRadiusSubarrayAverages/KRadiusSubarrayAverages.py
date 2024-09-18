# https://leetcode.com/problems/k-radius-subarray-averages/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        #Time: O(n), Space: O(n)
        curr = 0
        size = k*2+1
        ans = [-1 for _ in range(len(nums))]

        for i in range(len(nums)):
            curr+=nums[i]
            if i>=(size-1):
                ans[i-k]=curr//size
                curr-=nums[i-(size-1)]
        return ans

# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixCount={0:1}
        curr=0
        result=0

        for i in range(0, len(nums)):
            curr+=nums[i]
            result+=prefixCount.get(curr-k, 0)
            prefixCount[curr] = prefixCount.get(curr, 0)+1

        return result


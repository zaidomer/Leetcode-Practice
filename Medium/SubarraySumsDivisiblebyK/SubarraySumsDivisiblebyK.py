# https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0
        curr = 0
        prefix = {0: 1}
        for i in range(0, len(nums)):
            curr += nums[i]
            diff = curr % k
            result += prefix.get(diff, 0)
            prefix[diff] = prefix.get(diff, 0) + 1
        return result

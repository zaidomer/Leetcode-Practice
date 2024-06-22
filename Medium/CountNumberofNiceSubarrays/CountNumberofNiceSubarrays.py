# https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        numSubArrays=0
        sumVal=0
        prefixMap={0:1}
        for i in range(0, len(nums)):
            sumVal+=nums[i]%2
            diff=sumVal-k

            numSubArrays+=prefixMap.get(diff,0)
            prefixMap[sumVal]=prefixMap.get(sumVal,0)+1


        return numSubArrays
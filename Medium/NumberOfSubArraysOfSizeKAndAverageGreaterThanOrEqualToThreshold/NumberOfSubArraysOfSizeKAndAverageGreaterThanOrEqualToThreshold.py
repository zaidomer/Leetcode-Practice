# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr)<k:
            return 0

        target = threshold*k
        curr = 0
        res = 0
        left = 0

        for right in range(0, len(arr)):
            curr+=arr[right]
            if right<(k-1):
                continue
            if curr>=target:
                res+=1
            curr-=arr[left]
            left+=1

        return res
        
# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # target.sort()
        # arr.sort()
        # return target==arr

        return Counter(target)==Counter(arr)
        
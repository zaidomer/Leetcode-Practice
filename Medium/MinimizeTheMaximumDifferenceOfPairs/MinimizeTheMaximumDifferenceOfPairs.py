# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p==0:
            return 0

        nums.sort()
        l = 0
        r = 10**9
        res = r

        def canMakePairs(diff):
            i = 0
            pairs = 0
            while i<len(nums)-1:
                if nums[i+1]-nums[i]<=diff:
                    pairs+=1
                    if pairs==p:
                        return True
                    i+=2
                else:
                    i+=1
            return False

        while l<=r:
            mid = l + (r-l)//2
            if canMakePairs(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res
        
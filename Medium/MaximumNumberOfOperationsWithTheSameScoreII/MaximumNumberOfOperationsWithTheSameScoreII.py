# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        #Time: O(n^2), Space: O(n^2)
        cache = {}
  
        def dfs(l, r, score):
            if ((r+1)-l)<2:
                return 0
            elif (l, r) in cache:
                return cache[(l, r)]
                
            res = 0
            if nums[l]+nums[l+1]==score:
                res = max(res, 1+dfs(l+2, r, score))
            if nums[r]+nums[r-1]==score:
                res = max(res, 1+dfs(l, r-2, score))
            if nums[l]+nums[r]==score:
                res = max(res, 1+dfs(l+1, r-1, score))
            cache[(l, r)] = res
            return res
            
            
        return max(1+dfs(0, len(nums)-3, nums[-1]+nums[-2]), 1+dfs(2, len(nums)-1, nums[0]+nums[1]), 1+dfs(1, len(nums)-2, nums[0]+nums[-1]))

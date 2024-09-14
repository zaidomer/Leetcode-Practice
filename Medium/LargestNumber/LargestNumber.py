# https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        def comp(n1, n2):
            if n1+n2>n2+n1:
                return -1
            else:
                return 1

        nums.sort(key=cmp_to_key(comp))
        res = ''.join(nums)
        if res[0]=='0':
            return '0'
        return res

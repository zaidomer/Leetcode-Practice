# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        numOnes = 0
        for i in range(N):
            numOnes+=nums[i]
        
        left = 0
        right = 0
        onesInWindow = 0
        maxOnesInWindow = 0

        for right in range(N+numOnes-1):
            if nums[right%N]==1:
                onesInWindow+=1
            if right>=numOnes:
                onesInWindow-=nums[left%N]
                left+=1
            maxOnesInWindow = max(maxOnesInWindow, onesInWindow)
        return numOnes-maxOnesInWindow
        
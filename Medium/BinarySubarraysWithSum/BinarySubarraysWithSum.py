class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # VALID PREFIX SUM APPROACH
        # res = 0
        # prefixSum = defaultdict(int)
        # prefixSum[0]=1
        # currSum = 0

        # for i in range(len(nums)):
        #     currSum += nums[i]
        #     if currSum-goal in prefixSum:
        #         res+=prefixSum[currSum-goal]
        #     prefixSum[currSum]+=1

        # return res









        # VALID SLIDING WINDOW APPROACH
        def slidingWindow(target):
            if target<0:
                return 0
            res = 0
            currSum = 0
            left = 0
            for right in range(len(nums)):
                currSum += nums[right]
                while currSum>target and left<=right:
                    currSum -= nums[left]
                    left+=1
                res += right-left+1
            return res

        return slidingWindow(goal) - slidingWindow(goal-1)

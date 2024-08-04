# https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # dp = {}
        # dayMap = {costs[0]:1, costs[1]:7, costs[2]:30}

        # def computePlan(i:int):
        #     if i>=len(days):
        #         return 0
        #     elif i in dp:
        #         return dp[i]

        #     dp[i] = float("inf")
        #     for cost in costs:
        #         j=i
        #         while j<(len(days)) and days[j]<(days[i]+dayMap[cost]):
        #             j+=1

        #         dp[i] = min(dp[i], cost+computePlan(j))

        #     return dp[i]
            
        # return computePlan(0)






        dp = defaultdict(int)
        dayMap = {costs[0]:1, costs[1]:7, costs[2]:30}

        for i in range(len(days)-1, -1, -1):
            dp[i]=float("inf")
            for cost in costs:
                j=i
                while j<(len(days)) and days[j]<(days[i]+dayMap[cost]):
                    j+=1
                dp[i] = min(dp[i], cost+dp[j])
        
        return dp[0]
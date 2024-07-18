class Solution:
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     nextStep = cost[len(cost)-2]
    #     secondNextStep = cost[len(cost)-1]

    #     for i in range(len(cost)-3, -1, -1):
    #         temp = nextStep
    #         nextStep = cost[i] + min(nextStep, secondNextStep)
    #         secondNextStep = temp

    #     return min(nextStep, secondNextStep)
     
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        nextStep = cost[len(cost)-2]
        secondNextStep = cost[len(cost)-1]

        for i in range(len(cost)-3, -1, -1):
            temp = nextStep
            nextStep = cost[i] + min(nextStep, secondNextStep)
            secondNextStep = temp

        return min(nextStep, secondNextStep)

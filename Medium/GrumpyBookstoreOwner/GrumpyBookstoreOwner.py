class Solution:
    # def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
    #     bestStart = 0
    #     start=0
    #     maxDiff = 0
    #     result = 0
    #     potentialDiff=0
    #     default=0
    #     for i in range(0, len(grumpy)):
    #         potentialDiff+=customers[i]
    #         if i >= minutes:
    #             potentialDiff-=customers[start]
    #             if grumpy[start]==0:
    #                 default-=customers[start]
    #             start+=1

    #         if grumpy[i]==0:
    #             result+=customers[i]
    #             default+=customers[i]

    #         if potentialDiff-default > maxDiff:
    #             bestStart=start
    #             maxDiff=potentialDiff-default


    #     for i in range(bestStart, min(bestStart+minutes, len(grumpy))):
    #         if grumpy[i]:
    #             result+=customers[i]

    #     return result

    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total = 0
        for i in range(minutes):
            total += customers[i]

        for i in range(minutes, len(customers)):
            if grumpy[i] != 1:
                total += customers[i]
        
        output = total
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                total += customers[i]
            if grumpy[i-minutes] == 1:
                total -= customers[i-minutes]
            output = max(output, total)

        return output

        


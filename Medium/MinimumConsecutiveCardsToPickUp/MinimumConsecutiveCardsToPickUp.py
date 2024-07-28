# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        cardDict = {}
        result = float("inf")

        for i in range(len(cards)):
            if cards[i] in cardDict:
                result = min(result, 1+i-cardDict[cards[i]])
            cardDict[cards[i]] = i

        if result==float("inf"):
            return -1

        return result

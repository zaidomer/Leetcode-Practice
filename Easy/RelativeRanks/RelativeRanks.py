# https://leetcode.com/problems/relative-ranks/description/?envType=daily-question&envId=2024-05-08

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScores = sorted(score, reverse=True)
        positionMap = {}
        medalNames = {0:"Gold Medal", 1:"Silver Medal", 2:"Bronze Medal"}
        
        for i in range(0, len(sortedScores)):
            positionMap[sortedScores[i]] = medalNames.get(i, str(i+1))

        finalList = []
        for i in range(0, len(score)):
            finalList.append(positionMap[score[i]])

        return finalList
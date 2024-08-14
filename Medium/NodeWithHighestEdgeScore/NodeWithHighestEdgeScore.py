# https://leetcode.com/problems/node-with-highest-edge-score/

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        edgeScores = [0 for _ in range(len(edges))]

        for i in range(len(edges)):
            edgeScores[edges[i]]+=i

        resScore = edgeScores[0]
        resIndex = 0

        for i in range(1, len(edgeScores)):
            if edgeScores[i]>resScore:
                resScore = edgeScores[i]
                resIndex = i
        
        return resIndex

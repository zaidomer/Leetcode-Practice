# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        players = {'A':0, 'B':0}

        for i in range(1, len(colors)-1):
            if colors[i]==colors[i-1]==colors[i+1]:
                players[colors[i]]+=1

        return players['A']>players['B']

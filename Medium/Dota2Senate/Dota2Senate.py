# https://leetcode.com/problems/dota2-senate/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dQueue = deque()
        rQueue = deque()
        n = len(senate)

        for i in range(len(senate)):
            if senate[i]=='R':
                rQueue.append(i)
            else:
                dQueue.append(i)

        while dQueue and rQueue:
            dVal = dQueue.popleft()
            rVal = rQueue.popleft()
            if dVal<rVal:
                dQueue.append(dVal+n)
            else:
                rQueue.append(rVal+n)

        if dQueue:
            return 'Dire'
        else:
            return 'Radiant'        

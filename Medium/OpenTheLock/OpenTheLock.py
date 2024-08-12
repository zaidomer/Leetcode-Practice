# https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit = set(deadends)
        start = '0000'
        if start in visit or target in visit:
            return -1

        q = deque([start])
        moves = [(0,1),(0,-1),(1,1),(1,-1),(2,1),(2,-1),(3,1),(3,-1)]
        res = 0

        while q:
            for i in range(len(q)):
                currCode = q.popleft()
                if currCode==target:
                    return res
                for wheel,move in moves:
                    newCode = currCode[0:wheel] + str((ord(currCode[wheel])-ord('0') + move)%10) + currCode[wheel+1:]
                    if newCode in visit:
                        continue
                    q.append(newCode)
                    visit.add(newCode)
            res+=1
        
        return -1

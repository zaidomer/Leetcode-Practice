# https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ## METHOD WITH STACK (NEETCODE METHOD)
        # stack = deque()
        # pairs = [[position[i], speed[i]] for i in range(len(position))]
        # pairs.sort(reverse=True)    
        
        # for pair in pairs:
        #     arrivalTime = (target-pair[0])/pair[1]
        #     if not stack or stack[-1]<arrivalTime:
        #         stack.append(arrivalTime)

        # return len(stack)



        ## METHOD W/O STACK
        pairs = [[position[i], speed[i]] for i in range(len(position))]
        pairs.sort(reverse=True)
        latestArrivalTime = float("-inf")
        fleets=0
        
        for pair in pairs:
            arrivalTime = (target-pair[0])/pair[1]
            if latestArrivalTime < arrivalTime:
                latestArrivalTime = arrivalTime
                fleets+=1

        return fleets
    
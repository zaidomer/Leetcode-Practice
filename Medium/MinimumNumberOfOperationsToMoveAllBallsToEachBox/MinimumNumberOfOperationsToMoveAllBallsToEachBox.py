# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Time: O(n), Space: O(n), where n is number of balls
        res = [0 for _ in range(len(boxes))]

        right = 0
        numBalls = 0
        for i in range(len(boxes)-1, -1, -1):
            res[i]+=right
            if boxes[i]=='1':
                numBalls+=1
            right+=numBalls

        left = 0
        numBalls = 0
        for i in range(len(boxes)):
            res[i]+=left
            if boxes[i]=='1':
                numBalls+=1
            left+=numBalls

        return res

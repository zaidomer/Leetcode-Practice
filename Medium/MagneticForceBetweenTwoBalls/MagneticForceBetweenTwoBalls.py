# https://leetcode.com/problems/magnetic-force-between-two-balls

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 1 
        right = position[len(position)-1] - position[0]
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            last = position[0]
            balls = 1
            for i in range(1, len(position)):
                if (position[i] - last) >= mid:
                    last = position[i]
                    balls += 1
            if balls >= m:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result
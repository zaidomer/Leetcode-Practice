# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        result = -1

        while left<right:
            result = max(result, (right-left)*min(height[left], height[right]))
            
            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return result
        
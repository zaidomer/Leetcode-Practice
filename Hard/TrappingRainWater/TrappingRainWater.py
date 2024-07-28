# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height)-1
        maxLeft = height[left]
        maxRight = height[right]

        while left<right:
            if maxLeft<=maxRight:
                left+=1
                result+=max(0, maxLeft-height[left])
                maxLeft=max(maxLeft, height[left])
            else:
                right-=1
                result+=max(0, maxRight-height[right])
                maxRight=max(maxRight, height[right])

        return result
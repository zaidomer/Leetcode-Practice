# https://leetcode.com/problems/sliding-window-maximum/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = deque()

        for right in range(len(nums)):
            while window and nums[right]>nums[window[-1]]:
                window.pop()
            window.append(right)

            if window[0]<=(right-k):
                window.popleft()

            if right>=k-1:
                res.append(nums[window[0]])

        return res
        
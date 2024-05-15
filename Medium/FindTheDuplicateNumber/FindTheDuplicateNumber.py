# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break

        slow2=nums[0]
        while slow2!=slow:
            slow2=nums[slow2]
            slow=nums[slow]

        return slow
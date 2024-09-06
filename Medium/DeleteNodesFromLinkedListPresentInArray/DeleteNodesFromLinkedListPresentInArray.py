# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n+m) time O(n) space where n=len(nums) and m=list len
        dummy = ListNode()
        dummy.next = head
        nums = set(nums)

        temp = dummy
        while temp.next:
            if temp.next.val in nums:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return dummy.next

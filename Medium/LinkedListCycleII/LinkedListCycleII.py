# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        isCycle = False

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                isCycle=True
                break

        if not isCycle:
            return None

        fast = head
        while fast!=slow:
            fast = fast.next
            slow = slow.next

        return slow


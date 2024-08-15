# https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        lessTail = less

        dummy = ListNode(0,head)
        temp = dummy

        while temp:
            while temp.next and temp.next.val<x:
                lessTail.next = temp.next
                temp.next = temp.next.next
                lessTail = lessTail.next
                lessTail.next = None
            temp = temp.next
        
        lessTail.next = dummy.next
        return less.next

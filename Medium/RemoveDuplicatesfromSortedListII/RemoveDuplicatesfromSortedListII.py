# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1000, head)     
        prev=dummy

        while head and head.next:
            if head.val==head.next.val:
                while head.next and head.val==head.next.val:
                    head=head.next
                prev.next=head.next
            else:
                prev=prev.next
            
            head=head.next
        
        return dummy.next

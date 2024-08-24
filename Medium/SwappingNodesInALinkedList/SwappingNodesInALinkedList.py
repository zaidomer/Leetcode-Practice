# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        curr = head
        for i in range(k-1):
            curr = curr.next
        
        node1 = curr
        node2 = head
        while curr.next:
            curr = curr.next
            node2 = node2.next
        
        node1.val,node2.val = node2.val,node1.val
        return head

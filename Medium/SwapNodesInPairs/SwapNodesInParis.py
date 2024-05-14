# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        
        newHead = head.next
        temp = head
        prevTemp=None
        
        while temp and temp.next:
            second = temp.next
            temp.next = temp.next.next
            second.next = temp

            if prevTemp:
                prevTemp.next = second

            prevTemp = temp
            temp = temp.next

        return newHead
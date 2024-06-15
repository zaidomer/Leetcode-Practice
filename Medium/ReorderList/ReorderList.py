# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        mid = self.cutListInHalfGetMidpoint(head)
        if mid==head:
            return

        secondHalfReversedHead = self.reverse(mid)
        temp = head
        prev = None
        while temp:
            nextNode = temp.next
            temp.next = secondHalfReversedHead
            secondHalfReversedHead = secondHalfReversedHead.next
            temp.next.next = nextNode
            prev = temp.next
            temp = nextNode
        
        if secondHalfReversedHead:
            prev.next = secondHalfReversedHead

        return head
    
    def cutListInHalfGetMidpoint(self, head:Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        mid = head
        beforeMid = None
        updateMid = False 
        while temp:
            if updateMid:
                beforeMid=mid
                mid = mid.next
            updateMid = not updateMid
            temp = temp.next

        if beforeMid:
            beforeMid.next=None

        return mid
        
    def reverse(self, head:Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        nextNode = None

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev
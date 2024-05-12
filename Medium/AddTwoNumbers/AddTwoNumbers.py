# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        temp = None
        carry = 0
        while l1 or l2 or carry:
            nextVal=0
            if l1:
                nextVal += l1.val
            if l2:
                nextVal += l2.val

            nextVal += carry
            carry = nextVal//10

            if head==None:
                head = ListNode(nextVal%10)
                temp = head
            else:
                temp.next = ListNode(nextVal%10)
                temp = temp.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return head

            
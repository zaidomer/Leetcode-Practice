# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        l1r = self.reverse(l1)
        l2r = self.reverse(l2)

        carry = 0
        result = None
        iterator = None
        
        while carry>0 or l1r or l2r:
            num1=0
            num2=0

            if l1r is not None:
                num1 = l1r.val
                l1r = l1r.next
            if l2r is not None:
                num2 = l2r.val
                l2r = l2r.next

            value = (num1+num2+carry)%10
            carry = (num1+num2+carry)//10
            temp = ListNode(value)

            if result is None:
                result = temp
                iterator = result
            else:
                iterator.next = temp
                iterator = iterator.next

        return self.reverse(result)


    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        nextNode = None

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     curr = head
    #     nextNode = None
    #     prev = None

    #     while curr:
    #         nextNode = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = nextNode
        
    #     return prev

    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     head = self.reverse(head)
    #     dummy = ListNode(-1, head)
    #     prev = dummy
    #     temp = head
    #     count = 1

    #     while temp:
    #         if count==n:
    #             prev.next=temp.next
    #             break
    #         else:
    #             temp = temp.next
    #             prev = prev.next
    #             count+=1
        
    #     return self.reverse(dummy.next)

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        left = dummy
        right = head

        while n>0 and right:
            right = right.next
            n-=1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next

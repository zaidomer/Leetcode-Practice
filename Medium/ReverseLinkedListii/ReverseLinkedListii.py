# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    #     if left==right:
    #         return head

    #     ogHead = head
    #     leftBreak = None
        
    #     if left-2>=0:
    #         leftBreak = head

    #         i=0
    #         while leftBreak and i<max(left-2, 0):
    #             leftBreak = leftBreak.next
    #             i+=1

    #         head = leftBreak.next
        
    #     firstReversedNode = head
    #     newHead = None
    #     temp = None

    #     i=0
    #     while head and i<right-left+1:
    #         temp = newHead
    #         newHead = head
    #         head = head.next
    #         newHead.next = temp
    #         i+=1

    #     if leftBreak:
    #         leftBreak.next = newHead

    #     firstReversedNode.next = head

    #     if left==1:
    #         return newHead
    #     return ogHead

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
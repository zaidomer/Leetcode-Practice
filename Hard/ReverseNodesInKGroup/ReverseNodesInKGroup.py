# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ## GOOD SOLUTION, NEETCODE SOLUTION JUST WRITTEN OUT MORE SIMPLY
        # if not head:
        #     return head

        # def reverse(head:Optional[ListNode]) -> Optional[ListNode]:
        #     curr = head
        #     nextNode = None
        #     prev = None

        #     while curr:
        #         nextNode = curr.next
        #         curr.next=prev
        #         prev = curr
        #         curr = nextNode

        #     return prev
        
        # temp = head
        # headToRev = head
        # newHead = None
        # prevTail=None
        # while temp:
        #     for i in range(k-1):
        #         if temp:
        #             temp=temp.next
        #     if not temp:
        #         break

        #     prev=temp
        #     temp=temp.next
        #     prev.next=None

        #     revHead = reverse(headToRev)
        #     if not newHead:
        #         newHead = revHead
        #     if prevTail:
        #         prevTail.next = revHead
        #     prevTail = headToRev
        #     headToRev.next=temp    
        #     headToRev = headToRev.next
        
        # return newHead




        def getKth(node:ListNode, k:int):
            while node and k>0:
                node = node.next
                k-=1
            return node

        def reverseGroup(groupStart:ListNode, nextGroupStart:ListNode) -> None:
            curr = groupStart
            nextNode = None
            prev = nextGroupStart

            while curr!=nextGroupStart:
                nextNode = curr.next
                curr.next=prev
                prev = curr
                curr = nextNode

        
        dummy = ListNode(-1, head)
        prevGroupEnd = dummy

        while True:
            kth = getKth(prevGroupEnd, k)
            if not kth:
                break

            nextGroupStart = kth.next
            groupStart = prevGroupEnd.next
            reverseGroup(groupStart, nextGroupStart)

            temp = groupStart
            prevGroupEnd.next = kth
            prevGroupEnd = temp

        return dummy.next
        
# https://leetcode.com/problems/merge-nodes-in-between-zeros/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Making a new list
        # dummy = ListNode()
        # temp = dummy
        # while head:
        #     sumVal = 0
        #     head = head.next
        #     while head and head.val!=0:
        #         sumVal+=head.val
        #         head = head.next
            
        #     if sumVal>0:
        #         temp.next = ListNode(sumVal, None)
        #         temp = temp.next
        # return dummy.next


        #modify original list
        temp = head.next
        newHead = temp
        while head.next:
            head = head.next
            while temp and temp.val>0:
                temp = temp.next
                head.val+=temp.val
            
            if temp:
                temp = temp.next
            head.next=temp
        return newHead

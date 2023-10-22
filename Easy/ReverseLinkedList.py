#https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # temp = head
        # stack = []

        # if head is None:
        #     return head

        # while(temp is not None):
        #     stack.append(temp)
        #     temp = temp.next


        # temp = stack.pop()
        # newHead = ListNode(temp.val, None)
        # temp = newHead
        # while(len(stack) > 0):
        #     temp2 = stack.pop()
        #     temp.next = ListNode(temp2.val, None)
        #     temp = temp.next

        # return newHead

        current = head
        newList = None

        while current is not None:
            nextNode = current.next
            current.next = newList
            newList = current
            current = nextNode

        return newList
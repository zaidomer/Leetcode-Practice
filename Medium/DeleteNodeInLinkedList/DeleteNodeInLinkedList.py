# https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # prev = node
        # while node.next!=None:
        #     prev=node
        #     node.val = node.next.val
        #     node = node.next

        # prev.next = None
        
        node.val, node.next=node.next.val, node.next.next
# https://leetcode.com/problems/next-greater-node-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        stack = deque()
        res = []
        i=0

        while head:
            while stack and stack[-1][0]<head.val:
                value, index = stack.pop()
                res[index] = head.val
            res.append(0)
            stack.append((head.val, i))
            head = head.next
            i+=1
        return res

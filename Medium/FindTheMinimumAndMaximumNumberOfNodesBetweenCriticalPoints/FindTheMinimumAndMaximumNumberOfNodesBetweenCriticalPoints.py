# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = []
        count = 0
        lastCritical = None
        smallest=float('inf')
        largest=None
        first=None
        numCritical=0


        while head and head.next:
            prev = head
            head = head.next
            nextNode = head.next
            if nextNode is None:
                break
            count+=1
            if (prev.val < head.val > nextNode.val) or (prev.val > head.val < nextNode.val):
                
                if numCritical==0:
                    first = count
                else:
                    smallest=min(smallest, count-lastCritical)
                    largest = count-first

                numCritical+=1
                lastCritical=count

        if numCritical<2:
            return [-1, -1]
        else:
            return[smallest, largest]
        

        


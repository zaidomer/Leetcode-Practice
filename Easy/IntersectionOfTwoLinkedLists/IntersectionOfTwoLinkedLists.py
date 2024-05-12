# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # nodeSet=set()

        # while headA:
        #     nodeSet.add(headA)
        #     headA = headA.next

        # while headB:
        #     if headB in nodeSet:
        #         return headB
        #     headB = headB.next

        # return None

        sizeA = 0
        sizeB = 0

        tempA = headA
        tempB = headB
        
        while tempA:
            sizeA+=1
            tempA=tempA.next

        while tempB:
            sizeB+=1
            tempB=tempB.next

        diff = sizeA-sizeB

        if diff > 0:
            while diff > 0:
                headA = headA.next
                diff-=1
        else:
            diff*=-1
            while diff > 0:
                headB = headB.next
                diff-=1

        while headA:
            if headA==headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
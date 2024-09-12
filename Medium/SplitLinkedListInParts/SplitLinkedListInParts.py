# https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        #Time: O(n), Space: O(1) (O(k) if u include output size)
        res = [None for _ in range(k)]
        temp = head
        listLen = 0
        while temp:
            listLen+=1
            temp = temp.next
        
        temp = head
        for i in range(k):
            partHead = temp
            nodesNeeded = ceil(listLen/(k-i))-1
            for j in range(nodesNeeded):
                if temp is None:
                    break
                temp = temp.next

            res[i]=partHead
            if temp:
                newTemp = temp.next
                temp.next=None
                temp = newTemp
                listLen-=nodesNeeded+1
            else:
                return res
        return res          

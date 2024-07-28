# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # newHead = None
        # heap=[]
        # nodeDict = defaultdict(deque)

        # for temp in lists:
        #     while temp:
        #         heappush(heap, temp.val)
        #         nodeDict[temp.val].append(temp)
        #         temp = temp.next

        # temp=None
        # while heap:
        #     val = heappop(heap)
        #     node = nodeDict[val].pop()
        #     node.next=None
        #     if not newHead:
        #         newHead=node
        #         temp=newHead
        #     else:
        #         temp.next=node
        #         temp=temp.next

        # return newHead

        if not lists or len(lists)==0:
            return None


        def mergeLists(l1,l2) -> Optional[ListNode]:
            dummy=ListNode()
            temp = dummy

            while l1 and l2:
                if l1.val<l2.val:
                    temp.next = l1
                    l1=l1.next
                else:
                    temp.next = l2
                    l2=l2.next

                temp=temp.next

            if l1:
                temp.next=l1
            elif l2:
                temp.next=l2

            return dummy.next


        while len(lists)>1:
            merged=[]
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2= lists[i+1] if i+1<len(lists) else None
                merged.append(mergeLists(l1, l2))
            lists = merged
        
        return lists[0]

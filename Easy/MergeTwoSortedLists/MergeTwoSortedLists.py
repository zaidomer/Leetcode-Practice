# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        first = None
        second = None

        if list1.val <= list2.val:
            first = list1
            second = list2
        else:
            first = list2
            second = list1
        
        head = first
        
        while first.next is not None and second is not None:
            if first.next.val > second.val:
                temp = second
                second = second.next
                temp.next = first.next
                first.next = temp
            first = first.next

        if second is not None:
            first.next = second
        return head
        
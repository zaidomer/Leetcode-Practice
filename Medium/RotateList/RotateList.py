# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if not head:
        #     return head

        # dummy = ListNode(-1, head)
        # fast = head
        # slow = dummy
        # end = head
        # newHead = head

        # temp=head
        # listLen=0
        # while temp:
        #     listLen+=1
        #     temp = temp.next

        # k = k%listLen

        # for i in range(k):
        #     fast = fast.next
        #     if not fast:
        #         fast = head

        # while fast:
        #     end = fast
        #     fast = fast.next
        #     slow = slow.next

        # if slow.next:
        #     newHead = slow.next
        #     slow.next = None
        #     end.next = head

        # return newHead



        if not head:
            return head

        end = head
        newHead = head

        temp=head
        listLen=0
        while temp:
            listLen+=1
            end = temp
            temp = temp.next

        k = k%listLen
        temp = head
        end.next = head

        for i in range(listLen-k):
            head = head.next
            end = end.next

        end.next = None
        return head

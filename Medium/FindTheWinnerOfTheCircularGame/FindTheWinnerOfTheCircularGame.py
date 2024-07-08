# https://leetcode.com/problems/find-the-winner-of-the-circular-game/

#Original try
# class Node:
#     def __init__(self, val, next=None):
#         self.val=val
#         self.next=next

# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         start = Node(1, None)
#         temp = start
#         for i in range(2, n+1):
#             temp.next=Node(i, None)
#             temp = temp.next
#         temp.next=start

#         while start.next!=start:
#             iterator = start
#             prev = temp

#             for i in range(k-1):
#                 prev=iterator
#                 iterator = iterator.next

#             prev.next=iterator.next
#             start=iterator.next


#         return start.val



#Queue solution (EASIEST TO UNDERSTAND)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque()
        
        for i in range(1, n+1):
            q.append(i)

        while len(q)>1:
            for i in range(0, k-1):
                num = q.popleft()
                q.append(num)
            q.popleft()

        return q[0]    



# like queue solution but with array
# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         nums=list(range(n))
#         index=0

#         while len(nums)>1:
#             index = (index + k-1) % len(nums)
#             nums.pop(index)

#         return nums[0]+1






#Better approach (recursion)... O(n) time and space complexity
# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         if n == 1:
#             return 1
#         else:
#             return (self.findTheWinner(n-1, k)+k-1) % n + 1





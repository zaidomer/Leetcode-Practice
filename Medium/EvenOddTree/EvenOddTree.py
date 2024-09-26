# https://leetcode.com/problems/even-odd-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        #Time: O(n), Space: O(n)
        level = 0
        q = deque(([root]))
        
        while q:
            prev = float("-inf") if level%2==0 else float("inf")
            for i in range(len(q)):
                node = q.popleft()
                if (level%2==0 and (node.val<=prev or node.val%2==0)) or (level%2!=0 and (node.val>=prev or node.val%2!=0)):
                    return False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                prev = node.val
            level+=1
        return True

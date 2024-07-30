# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ## VALID BFS SOLUTION
        # pQ = deque([p])
        # qQ = deque([q])

        # while pQ and qQ:
        #     for i in range(len(pQ)):
        #         pNode = pQ.popleft()
        #         qNode = qQ.popleft()

        #         if (pNode and qNode is None) or (qNode and pNode is None) or (pNode and qNode and pNode.val!=qNode.val):
        #             return False
                
        #         if pNode and qNode:
        #             pQ.append(pNode.left)
        #             qQ.append(qNode.left)

        #             pQ.append(pNode.right)
        #             qQ.append(qNode.right)
        # return len(pQ)==len(qQ)==0








        ## VALID DFS SOLUTION
        if p is None and q is None:
            return True
        elif p is None or q is None or p.val!=q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
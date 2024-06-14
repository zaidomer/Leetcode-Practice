# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 


class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        return self.traverse(root, -999999, [0])

    def traverse(self, root: TreeNode, maxVal: int, count: List[int]) -> int:
        if root is None:
            return count[0]

        if root.val>=maxVal:
            count[0]+=1

        maxVal=max(root.val, maxVal)
        
        self.traverse(root.left, maxVal, count)
        self.traverse(root.right, maxVal, count)       

        return count[0]

        

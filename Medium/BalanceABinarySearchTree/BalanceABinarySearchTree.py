# https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        treeArr = []
        self.traverse(root, treeArr)
        return self.buildTree(treeArr, 0, len(treeArr)-1)

    def traverse(self, root:TreeNode, treeArr: List[TreeNode]) -> None:
        if root is None:
            return
        self.traverse(root.left, treeArr)
        treeArr.append(root.val)
        self.traverse(root.right, treeArr)
        
    def buildTree(self, treeArr: List[int], leftIndex: int, rightIndex: int) -> TreeNode:
        if leftIndex>rightIndex:
            return None
        mid = leftIndex+(rightIndex-leftIndex)//2
        return TreeNode(treeArr[mid], self.buildTree(treeArr, leftIndex, mid-1), self.buildTree(treeArr, mid+1, rightIndex))

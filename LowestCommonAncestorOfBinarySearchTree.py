#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        

        max = -1
        min = -1
        if(p.val > q.val):
            max = p
            min = q
        else:
            max = q
            min = p

        # print(root.val)
        # print(str(max.val) + ", " + str(min.val))

        if(root is None):
            return root

        if((root.val <= max.val) and (root.val >= min.val)):
            return root
        elif(root.val > max.val and root.left is not None):
            return self.lowestCommonAncestor(root.left, p, q)
        elif(root.val < min.val and root.right is not None):
            return self.lowestCommonAncestor(root.right, p, q)
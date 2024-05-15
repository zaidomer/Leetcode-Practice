# https://leetcode.com/problems/subtree-of-another-tree/

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None :
            return True

        if root == None :
            return False

        if self.same(root , subRoot):
            return True
        return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot)            

    def same(self , root , subRoot):
        if root == None and subRoot == None :
            return True

        if root and subRoot and root.val == subRoot.val:
            return self.same(root.right , subRoot.right) and self.same(root.left , subRoot.left)  

        return False
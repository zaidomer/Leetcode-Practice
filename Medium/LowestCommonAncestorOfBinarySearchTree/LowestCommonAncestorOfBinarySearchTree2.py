#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp = root
        while temp is not None:
            if temp.val < p.val and temp.val < q.val:
                temp = temp.right
            elif temp.val > p.val and temp.val > q.val:
                temp = temp.left
            else:
                return temp
        
        return None
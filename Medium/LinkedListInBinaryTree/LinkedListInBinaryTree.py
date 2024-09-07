# https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        #Initial attampt, prob O(m+nm) time and space
        # listPath = ""
        # while head:
        #     listPath+=str(head.val)+','
        #     head = head.next
        
        # def dfs(treeNode, path):
        #     if path==listPath:
        #         return True
        #     elif treeNode is None:
        #         return False
            
        #     path+=str(treeNode.val)+','
        #     return dfs(treeNode.right, path[-len(listPath):]) or dfs(treeNode.left, path[-len(listPath):])

        # return dfs(root, "")










        # Time: O(nm) Space: O(nm)
        def same(treeNode, listNode):
            if listNode is None:
                return True
            elif treeNode is None or treeNode.val!=listNode.val:
                return False
            return same(treeNode.left, listNode.next) or same(treeNode.right, listNode.next)

        def dfs(treeNode, listNode):
            if same(treeNode, listNode):
                return True
            elif treeNode is None:
                return False
            return dfs(treeNode.left, listNode) or dfs(treeNode.right, listNode)

        return dfs(root, head)

# https://leetcode.com/problems/create-binary-tree-from-descriptions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodeMap = {}
        isChild = {}
        
        for node in descriptions:
            #setup parent
            if node[0] not in nodeMap:
                nodeMap[node[0]] = TreeNode(node[0], None, None)
                isChild[node[0]] = False
            parent = nodeMap[node[0]]


            #setup child
            if node[1] not in nodeMap:
                nodeMap[node[1]] = TreeNode(node[1], None, None)
            child = nodeMap[node[1]]
            isChild[node[1]]=True

            
            #add child to parent
            if node[2]:
                parent.left = child
            else:
                parent.right = child
        

        for key in isChild:
            if not isChild[key]:
                return nodeMap[key]

        return None


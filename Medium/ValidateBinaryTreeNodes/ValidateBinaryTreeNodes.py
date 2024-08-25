# https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        hasParent = set(leftChild + rightChild)
        hasParent.discard(-1)
        if len(hasParent)!=n-1:
            return False
        visit = set()

        root = -1
        for i in range(n):
            if i not in hasParent:
                root = i
                break

        def dfs(node):
            if node==-1:
                return True
            elif node in visit:
                return False
            visit.add(node)
            return dfs(leftChild[node]) and dfs(rightChild[node])

        return dfs(root) and len(visit)==n

# https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        #O(n) time and space complexity
        
        prefixSum = defaultdict(int)
        prefixSum[0]+=1

        def dfs(node, currSum):
            count = 0
            if node:
                currSum+=node.val
                count+=prefixSum[currSum-targetSum]
                prefixSum[currSum]+=1
                count += dfs(node.left, currSum) + dfs(node.right, currSum)
                prefixSum[currSum]-=1
            return count
        
        return dfs(root, 0)

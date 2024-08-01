# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        nodeDict = {}

        def dfs(node:Optional['Node']):
            if node in nodeDict:
                return nodeDict[node]
            
            copy = Node(node.val, [])
            nodeDict[node] = copy
            for nei in node.neighbors:
                nodeDict[node].neighbors.append(dfs(nei))
            return copy

        dfs(node)
        return nodeDict[node]
        
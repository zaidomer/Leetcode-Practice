# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':  
        nodesMap=defaultdict(lambda: Node(0,None,None))
        nodesMap[None]=None
        temp = head

        while temp:
            node = nodesMap[temp]
            node.val = temp.val
            node.next = nodesMap[temp.next]
            node.random = nodesMap[temp.random]
            temp = temp.next

        return nodesMap[head]

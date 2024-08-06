# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = defaultdict(list)
        for src,dst in edges:
            incoming[dst].append(src)

        res = []
        for i in range(n):
            if i not in incoming:
                res.append(i)
        return res

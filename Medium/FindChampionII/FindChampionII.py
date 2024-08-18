# https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src,dst in edges:
           graph[dst].append(src)

        res = -1
        for i in range(0, n):
            if len(graph[i])==0:
                if res==-1:
                    res = i
                else:
                    return -1
        return res
        
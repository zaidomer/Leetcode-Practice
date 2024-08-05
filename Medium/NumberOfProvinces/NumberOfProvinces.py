# https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ## VALID BFS APPROACH
        # n=len(isConnected)
        # visit=set()
        # q = deque()
        # result = 0

        # for i in range(n):
        #     if i in visit:
        #         continue
        #     result+=1
        #     q.append(i)
        #     visit.add(i)

        #     while q:
        #         node = q.popleft()
        #         for j in range(n):
        #             if j not in visit and isConnected[node][j]:
        #                 q.append(j)
        #                 visit.add(j)

        # return result












        ## VALID DFS APPROACH
        visit = set()
        n=len(isConnected)
        result = 0

        def dfs(node, visit):
            visit.add(node)
            for i in range(n):
                if isConnected[node][i] and i not in visit:
                    dfs(i, visit)

        for i in range(n):
            if i in visit:
                continue
            result+=1
            dfs(i, visit)
            if len(visit)==n:
                break

        return result

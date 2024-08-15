# https://leetcode.com/problems/jump-game-iii/

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        ## VALID BFS APPROACH
        # q = deque([start])
        # visit = set()
        # while q:
        #     i = q.popleft()
        #     if arr[i]==0:
        #         return True
            
        #     right = i+arr[i]
        #     left = i-arr[i]
        #     if right<len(arr) and right not in visit:
        #         q.append(right)
        #         visit.add(right)
        #     if left>=0 and left not in visit:
        #         q.append(left)
        #         visit.add(left)
        # return False












        ## VALID DFS APPROACH
        visit = set()
        def dfs(i):
            if i in visit or i<0 or i>=len(arr):
                return False
            elif arr[i]==0:
                return True
            
            visit.add(i)
            return dfs(i-arr[i]) or dfs(i+arr[i])

        return dfs(start)

# https://leetcode.com/problems/task-scheduler/description/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        map = [0 for i in range(26)]

        for i in range(0,len(tasks)):
            map[ord(tasks[i]) - ord('A')] += 1

        map.sort()
        mostFrequent = map[25] - 1
        idle = mostFrequent * n

        for i in range(24, -1, -1):
            idle -= min(mostFrequent, map[i])

        if idle >= 0:
            return len(tasks) + idle 

        return len(tasks)
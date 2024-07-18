# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.courseMap = defaultdict(list)

        for req in prerequisites:
            self.courseMap[req[0]].append(req[1])

        for i in range(0, numCourses):
            if not self.check(i, set()):
                return False

        return True

    def check(self, course:int, path:Set[int]):
        if course in path:
            return False

        prereqs = self.courseMap[course]
        if prereqs==[]:
            return True
        
        path.add(course)
        for pre in prereqs:
            if not self.check(pre, path):
                return False
        path.remove(course)
        self.courseMap[course]=[]
        return True
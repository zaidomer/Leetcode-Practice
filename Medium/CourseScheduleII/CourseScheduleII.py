# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        resultSet = set(result)

        courseMap = defaultdict(list)
        for course in prerequisites:
            courseMap[course[0]].append(course[1])


        def dfs(course: int, visit:Set[int]) -> bool:
            if course in visit:
                return False
            if course in resultSet:
                return True

            visit.add(course)
            for pre in courseMap[course]:
                if not dfs(pre, visit):
                    return False

            visit.remove(course)
            resultSet.add(course)
            result.append(course)

            return True
        

        for course in range(0, numCourses):
            if not dfs(course, set()):
                return []

        return result

        
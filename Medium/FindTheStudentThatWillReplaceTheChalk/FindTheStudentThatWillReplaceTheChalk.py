# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalkNeeded = sum(chalk)
        extra = k%chalkNeeded

        for i in range(len(chalk)):
            extra-=chalk[i]
            if extra<0:
                return i
        return 0

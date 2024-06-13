# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        count = 0
        seats.sort()
        students.sort()

        for i in range(0, len(students)):
            count+=abs(seats[i]-students[i])

        return count
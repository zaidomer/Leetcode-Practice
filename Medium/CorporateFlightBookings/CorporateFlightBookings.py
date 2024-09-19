class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        #Time: O(n), Space: O(n)
        res = [0 for _ in range(n)]
        for i,j,k in bookings:
            res[i-1] += k
            if j<n:
                res[j] -= k

        for i in range(1,n):
            res[i] += res[i-1]
        return res
    
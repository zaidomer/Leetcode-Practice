class Solution:
    def knightDialer(self, n: int) -> int:
        # numbers = 0
        # phone = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]
        # directions = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        # dp = {}

        # def move(digit, dr, dc):
        #     if digit==0:
        #         digit = 11
        #     r = (digit-1)//3 + dr
        #     c = (digit-1)%3 + dc
        #     if (r==3 and c==1) or (r>=0 and r<=2 and c>=0 and c<=2):
        #         return phone[r][c]
        #     return -1

        # def dial(digit, remaining):
        #     if digit<0:
        #         return 0
        #     elif (digit,remaining) in dp:
        #         return dp[(digit,remaining)]
        #     elif remaining==0:
        #         return 1
            
        #     res = 0
        #     for dr,dc in directions:
        #         res += dial(move(digit, dr, dc), remaining-1)
        #     dp[(digit,remaining)] = res
        #     return res


        # for i in range(10):
        #     numbers+=dial(i, n-1)
        # return numbers%(10**9 + 7)











        if n==1:
            return 10

        mod = 10**9+7
        jumps = [[4,6],[8,6],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
        dp = [1 for _ in range(10)]

        for i in range(n-1):
            nextDp = [0 for _ in range(10)]
            for j in range(10):
                for k in jumps[j]:
                    nextDp[k] = (nextDp[k]+dp[j])%mod
            dp = nextDp

        res = 0
        for i in dp:
            res = (res+i)%mod
        return res

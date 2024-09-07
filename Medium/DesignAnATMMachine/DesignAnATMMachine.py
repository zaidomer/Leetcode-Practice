# https://leetcode.com/problems/design-an-atm-machine/?envType=problem-list-v2&envId=design

class ATM:

    def __init__(self):
        self.denominations = [20, 50, 100, 200, 500]
        self.notes = [0 for _ in range(5)]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.notes[i]+=banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        res = [0 for _ in range(5)]
        for i in range(len(self.denominations)-1, -1, -1):
            numNotes = min(self.notes[i], amount // self.denominations[i])
            res[i] = numNotes
            amount -= (numNotes * self.denominations[i])
        if amount == 0:
            self.deposit([-x for x in res])
            return res
        return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
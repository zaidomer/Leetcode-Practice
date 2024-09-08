# https://leetcode.com/problems/product-of-the-last-k-numbers/

class ProductOfNumbers:

    #Time: O(1), Space: O(n)
    def __init__(self):
        self.product = []

    #Time: O(1), Space: O(1)
    def add(self, num: int) -> None:
        if num==0:
            self.product=[]
        elif len(self.product)==0:
            self.product.append(num)
        else:
            self.product.append(self.product[-1]*num)

    #Time: O(1), Space: O(1)
    def getProduct(self, k: int) -> int:
        if k==len(self.product):
            return self.product[-1]
        elif k>len(self.product):
            return 0
        numsBeforeK = len(self.product)-1-k
        return self.product[-1]//self.product[numsBeforeK]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
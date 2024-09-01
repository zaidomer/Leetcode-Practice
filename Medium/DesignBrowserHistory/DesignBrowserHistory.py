# https://leetcode.com/problems/design-browser-history/

# class Page:
#     def __init__(self, url):
#         self.url = url
#         self.next = None
#         self.prev = None

# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.head = Page(homepage)
#         self.curr = self.head

#     def visit(self, url: str) -> None:
#         newPage = Page(url)
#         newPage.prev = self.curr
#         self.curr.next = newPage
#         self.curr = self.curr.next

#     def back(self, steps: int) -> str:
#         while steps>0 and self.curr!=self.head:
#             self.curr = self.curr.prev
#             steps-=1
#         return self.curr.url

#     def forward(self, steps: int) -> str:
#         while steps>0 and self.curr.next!=None:
#             self.curr = self.curr.next
#             steps-=1
#         return self.curr.url













class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.len = 1
        self.i = 0

    def visit(self, url: str) -> None:
        if len(self.history) < self.i+2:
            self.history.append(url)
        else:
            self.history[self.i+1] = url
        self.i+=1
        self.len=self.i+1

    def back(self, steps: int) -> str:
        self.i = max(self.i-steps, 0)
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.i+steps, self.len-1)
        return self.history[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
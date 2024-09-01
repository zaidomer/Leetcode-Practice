# https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    # def __init__(self, root: Optional[TreeNode]):
    #     self.root = root
    #     self.ptr = -1

    # def search(self, num):
    #     curr = self.root
    #     res = -1
    #     while curr:
    #         if curr.val==num:
    #             num = curr.val
    #             return curr.val
    #         elif curr.val>num:
    #             res = curr.val
    #             curr = curr.left
    #         else:
    #             curr = curr.right
    #     return res

    # def next(self) -> int:
    #     self.ptr+=1
    #     res = self.search(self.ptr)
    #     self.ptr = res
    #     return res


    # def hasNext(self) -> bool:
    #     return self.search(self.ptr+1)>=0









    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque()
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        res = self.stack.pop()
        curr = res.right
        while curr:
            self.stack.append(curr)
            curr = curr.left
        return res.val

    def hasNext(self) -> bool:
        return len(self.stack)>0

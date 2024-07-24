# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = []
        # for num in nums:
        #     heappush(heap, -num)

        # res = 0
        # for i in range(k):
        #     res = -heappop(heap)

        # return res





        # numDict = Counter(nums)
        # minVal = min(nums)
        # maxVal = max(nums)

        # for i in range(maxVal, minVal-1, -1):
        #     if i in numDict:
        #         k-=numDict[i]
        #         if k<=0:
        #             return i

        # return 0






        # ## Technincally most optimal but wont work on last test case
        # k = len(nums)-k

        # def quickSelect(l:int, r:int) -> int: #nums[r] used as pivot point
        #     swapIndex = l

        #     for i in range(l,r):
        #         if nums[i]<=nums[r]:
        #             nums[swapIndex], nums[i] = nums[i], nums[swapIndex]
        #             swapIndex+=1
            
        #     nums[swapIndex], nums[r] = nums[r], nums[swapIndex]

        #     if swapIndex>k:
        #         return quickSelect(l,swapIndex-1)
        #     elif swapIndex<k:
        #         return quickSelect(swapIndex+1,r)
        #     else:
        #         return nums[k]

        # return quickSelect(0, len(nums)-1)






        #Modified quick select
        left, mid, right = [],[],[]
        pivot = random.choice(nums)
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                mid.append(pivot)
            
        if k <= len(right): 
            return self.findKthLargest(right,k)
        elif k <= len(right) + len(mid) : 
            return pivot
        else: 
            return self.findKthLargest(left, k - len(right) - len(mid))

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(0,len(nums)):
            retrieved = map.get(target-nums[i])
            if retrieved!=None:
                return [i, retrieved]
            map[nums[i]] = i

        return []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            newNumber = target - nums[i]
            if newNumber in hashmap:
                return [i, hashmap[newNumber]]
            hashmap[nums[i]] = i
        return []

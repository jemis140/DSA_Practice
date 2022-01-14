class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        unique_element = 0
        for current in range(len(nums)):
            if nums[current] != nums[unique_element]:
                unique_element += 1
            nums[unique_element] = nums[current]
        return unique_element + 1
            
        
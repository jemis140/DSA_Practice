class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        sum_array = sum(nums)
        n = len(nums)
        
        if sum_array % 2 != 0:
            return False
        
        dp = set()
        dp.add(0)
        target = sum_array//2
        
        for i in range(len(nums)):
            nextDp =set()
            for t in dp:
                nextDp.add(nums[i] + t )
                nextDp.add(t)
            dp =nextDp
        return True if target in dp else False
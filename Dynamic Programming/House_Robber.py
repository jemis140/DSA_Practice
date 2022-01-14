class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return nums[0]
        
        elif n == 2:
            return max(nums[0], nums[1]);
        
        
        # Memo table setup
        memo = [None]*n
        memo[0] = nums[0];
        memo[1] = max(nums[0], nums[1]);
        
        # DP recurrence using memoization
        for i in range(2,n): 
            memo[i] = max(nums[i] + memo[i-2], memo[i-1])
        
        return memo[n-1];
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = [None]*n, [None]*n
        
        a = []
        
        l[0] = 1
        for i in range(1,n):
            l[i] = l[i-1]*nums[i-1]
            
        r[n-1] = 1   
        for j in range(n-2, -1, -1):
            r[j] = r[j+1]*nums[j+1]
        
        for i in range(n):
            a.append(l[i]*r[i])
        return a
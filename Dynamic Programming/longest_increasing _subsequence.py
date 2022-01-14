class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1]*n

        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j]+1

        maximum = 0

        for i in range(n):
            maximum = max(maximum, lis[i])

        return maximum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = [[]]
        n = len(nums)
 
        for i in range(0, n-2):

            l = i + 1

            # index of the last element
            r = n-1
            while (l < r):
                t = nums[i] + nums[l] + nums[r]
                if( t == 0):
                    result.append([nums[i],nums[l],nums[r]])

                elif (t < 0):
                    l += 1
                else:
                    r -= 1

        return r
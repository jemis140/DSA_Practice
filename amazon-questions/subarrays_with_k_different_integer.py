# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A good array is an array where the number of different integers in that array is exactly k.

# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

class Solution:
    def subarraysWithKDistinct(Self, A, K):
        def atMost(K):
            count = collections.Counter()
            res = i = 0
            for j in range(len(A)):
              # check for diffenet elements
                if count[A[j]] == 0:
                  # decrease the k to keep the track of different elements
                    K -= 1
                count[A[j]] += 1
                # if K becomes less than zero that means we need to decrease the window, remove array from begininng, update count, if it's becomes zero than we have availability for one more element
                while K < 0:
                    count[A[i]] -= 1
                    if count[A[i]] == 0:
                        K += 1
                    i += 1
                # add into result if we have subarray with K or less K different integers
                res += j - i + 1
            return res
        return atMost(K) - atMost(K-1)

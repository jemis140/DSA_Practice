# A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

# Return the minimum number of flips to make s monotone increasing.

# Solution: We will keep the minimum flip requires till ith index based on number of ones and zeroes

class Solution:
    def minFlipsMonoIncr(self, s):
        oneCount = 0
        flips = 0
        ans = 0
        for char in s:
            if char == '1':
                oneCount += 1
            else:
                flips += 1
            flips = min([flips, oneCount])
        return flips

# Solution: prefix sum
# In first half flip 1s to 0s and in second half flips all 0s to 1s take the minimum of operation


class Solution:
    def minFlipsMonoIncr(self, s):
        prefix = [0] * (len(s) + 1)
        ans = float("inf")
        for charIndex in range(0, len(s)):
            prefix[charIndex + 1] = prefix[charIndex] + \
                (1 if s[charIndex] == '1' else 0)

        for prefixIndex in range(0, len(s) + 1):
            ans = min([ans, prefix[prefixIndex] + len(s) -
                      prefixIndex - (prefix[len(s)] - prefix[prefixIndex])])
        return ans

# Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

# Substrings that occur multiple times are counted the number of times they occur.
# Solution: group strings of all 0's and 1's
class Solution:
    def countBinarySubstrings(self, s):
        binaryChunks = s.replace("01", "0 1").replace("10", "1 0").split()
        ans = 0
        print(binaryChunks)
        for chunkIndex in range(1, len(binaryChunks)):
            ans += min(len(binaryChunks[chunkIndex - 1]),
                       len(binaryChunks[chunkIndex]))
        return ans

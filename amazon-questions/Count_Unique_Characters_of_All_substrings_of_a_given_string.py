# Let's define a function countUniqueChars(s) that returns the number of unique characters on s.

# For example if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
# Given a string s, return the sum of countUniqueChars(t) where t is a substring of s.

# Notice that some substrings can be repeated so in this case you have to count the repeated ones too.
# Solution: https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/1505263/Single-pass-O(n)-time-and-O(1)-space-solution-with-detailed-explanation
class Solution:
    def uniqueLetterString(self, s):
        lastSeen = {}
        retval = 0
        lastStepCount = 0
        for i in range(len(s)):
            lastTwoSeenIndices = lastSeen.get(s[i], None)
            if not lastTwoSeenIndices:
                currentStepCount = lastStepCount + i + 1
                lastSeen[s[i]] = (-1, i)
            else:
                secondLastOccurance, lastSeenIndex = lastTwoSeenIndices
                numOfSuffixesWithoutCurrChar = i - 1 - lastSeenIndex
                numOfSuffixesWithJustOneOccurrenceOfCurrChar = lastSeenIndex - secondLastOccurance
                currentStepCount = lastStepCount + 1 + numOfSuffixesWithoutCurrChar - \
                    numOfSuffixesWithJustOneOccurrenceOfCurrChar
                lastSeen[s[i]] = (lastSeenIndex, i)
            retval += currentStepCount
            lastStepCount = currentStepCount
        return retval

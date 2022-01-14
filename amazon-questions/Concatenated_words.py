# Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.
class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        words = sorted(words, key=lambda word: len(word))
        wordSet = {}
        ans = []
        for word in words:
            if self.canForm(word, wordSet):
                ans.append(word)
            wordSet[word] = 1
        return ans

    def canForm(self, word, wordSet):
        if len(wordSet.keys()) == 0:
            return False
        dp = [False] * (len(word) + 1)
        dp[0] = True
        for outerIndex in range(1, len(word) + 1):
            for innerIndex in range(0, outerIndex):
                if not dp[innerIndex]:
                    continue
                if word[innerIndex:outerIndex] in wordSet:
                    dp[outerIndex] = True
                    break
        return dp[len(word)]


class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        dictionary = set(words)

        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in dictionary and suffix in dictionary:
                    return True
                if prefix in dictionary and dfs(suffix):
                    return True
            return False
        result = []

        for word in words:
            if dfs(word):
                result.append(word)
        return result

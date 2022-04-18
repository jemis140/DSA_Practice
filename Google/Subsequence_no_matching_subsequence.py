# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# Example 1:
# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n_subsequences = 0
        state = defaultdict(list)
        for word in words:
            state[word[0]].append(word[1:])
        for char in s:
            old_bucket = state[char]
            state[char] = []
            for suffix in old_bucket:
                if not suffix:
                    n_subsequences += 1
                else:
                    state[suffix[0]].append(suffix[1:])
        return n_subsequences
        
# // DNA is a long molecule that consists of a string of units called nucleotides. There are 4 types
# // of nucleotides, represented by the letters "A", "T", "C", and "G". Given two inputs: an arbitrary
# // DNA sequence and a list of DNA fragments, return true if the sequence can be constructed
# // using some combination of the fragments, false otherwise.

# // Examples:

# // Input: "GTCAGAG", ["GTC", "AG"]
# // Returns: True

# // Input: "GTCAGAG", ["GTCA", "AGAG"]

# // Returns: False
# Solution 1 using BFS
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        q = deque()
        visited = set()

        q.append(0)
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    q.append(end)
                    if end == len(s):
                        return True
            visited.add(start)
        return False

#Solution 2: Dynammic Programming

def sequenceConstruction (word, tiles):
  # Check for base cases here

  lettersMatched = 0
  expectedMatches = len(word)
  currSubstring = ""

  for char in word:
    currSubstring += char
    if currSubstring in tiles:
      word = word[len(currSubstring):]
      lettersMatched += len(currSubstring)
      currSubstring = ""

  return lettersMatched == expectedMatches
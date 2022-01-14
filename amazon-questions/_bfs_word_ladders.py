# Starts with beginword
# we check the word is end then we return the level
# else find all adjcent words which are in dictionary and not visited, add all into queue
# perform this until we find endWord
class Solution:
    def generateNeighbors(self, word):
        result = []
        for cIndex in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                result.append(word[:cIndex] + c + word[cIndex + 1:])
        return result

    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        deq = deque([beginWord])
        seen = set()

        level = 0

        while deq:
            size = len(deq)

            for _ in range(size):
                word = deq.popleft()
                seen.add(word)

                if word == endWord:
                    return level + 1

                neighbors = self.generateNeighbors(word)

                for neigh in neighbors:
                    if neigh in wordList and neigh not in seen:
                        deq.append(neigh)
                        seen.add(neigh)
            level += 1

        return 0


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        deq = collections.deque([[beginWord, 1]])

        while deq:
            word, length = deq.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        deq.append([next_word, length + 1])

        return 0

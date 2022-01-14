# Problem:https://leetcode.com/problems/word-search-ii/
# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for c in word:
            node = node.children[c]

        node.isWord = True


class Solution:
    def findWords(self, board, words):
        totalRows = len(board)
        totalColumns = len(board[0])
        trie = Trie()
        root = trie.root
        for word in words:
            trie.insert(word)

        result = []

        def dfs(rowIndex, columnIndex, node, path):
            if node.isWord:
                result.append(path)
                node.isWord = False

            if rowIndex < 0 or rowIndex >= totalRows or columnIndex < 0 or columnIndex >= totalColumns:
                return

            temp = board[rowIndex][columnIndex]
            node = node.children.get(temp)

            if not node:
                return

            board[rowIndex][columnIndex] = "#"

            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                newX = rowIndex + dx
                newY = columnIndex + dy
                dfs(newX, newY, node, path + temp)

            board[rowIndex][columnIndex] = temp

        for rowIndex in range(totalRows):
            for columnIndex in range(totalColumns):
                dfs(rowIndex, columnIndex, root, "")

        return result

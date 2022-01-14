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
    def exist(self, board: List[List[str]], word: str) -> bool:
        totalRows = len(board)
        totalColumns = len(board[0])
        trie = Trie()
        root = trie.root
        result = []

        trie.insert(word)

        isFound = False

        def dfs(rowIndex, columnIndex, node, path):
            if node.isWord:
                result.append(path)
                node.isWord = False

            if rowIndex < 0 or rowIndex >= totalRows or columnIndex < 0 or columnIndex >= totalColumns:
                return

            c = board[rowIndex][columnIndex]
            node = node.children.get(c)

            if not node:
                return

            board[rowIndex][columnIndex] = "$"

            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                newX, newY = rowIndex + dx, columnIndex + dy
                dfs(newX, newY, node, path + c)

            board[rowIndex][columnIndex] = c

        for rowIndex in range(totalRows):
            for columnIndex in range(totalColumns):
                dfs(rowIndex, columnIndex, root, "")

        return result

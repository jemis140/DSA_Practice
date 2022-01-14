# Given an array of strings products and a string searchWord.
# We want to design a system that suggests at most three product names from products after each character of searchWord is typed.
# Suggested products should have common prefix with the searchWord.
# If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return list of lists of the suggested products after each character of searchWord is typed.

# Missed Edge Cases: none
from collections import defaultdict


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        answer = []
        searchString = ''
        for char in searchWord:
            searchString += char
            result = []
            result = list(
                filter(lambda product: product.startswith(searchString), products))[:3]
            answer.append(result)
        return answer


class TrieNode:

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.suggestions = []

    def add_suggestion(self, item):
        if len(self.suggestions) < 3:
            self.suggestions.append(item)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        products.sort()
        root = TrieNode()
        for p in products:
            node = root

            for ch in p:
                node = node.children[ch]
                node.add_suggestion(p)

        res = []
        node = root
        for ch in searchWord:
            node = node.children[ch]
            res.append(node.suggestions)

        return res

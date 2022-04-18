from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        def DFSutil(words, memo, currentWord):
             # If currentWord was encountered previously we just return its corresponding value in the map memo.
            if currentWord in memo.keys():
                return memo[currentWord]
            
            maxLength =1
            
            for i in range(len(currentWord)):
                newWord =  currentWord[:i] + currentWord[i+1:]
                
                if newWord in words:
                    currentLength = 1 + DFSutil(words, memo, newWord)
                    maxLength = max(maxLength, currentLength)
                    
                memo[currentWord] = maxLength
            return maxLength
        #Initialize a set (wordsPresent) and add all the words in the list to the set. This set will be used to check if a word is present in the list.
        wordPresent = list(set(words))
        #Initialize a map (memo) having key type as String and value type as Integer. This map will store the length of the longest possible word sequence where the key is the last word in the sequence.
        memo = defaultdict(int)

        ans = 1
        #Iterate over the list. For each word in the list perform a depth-first search.
        for w in words:
            ans = max(ans, DFSutil(wordPresent, memo, w))
        return ans
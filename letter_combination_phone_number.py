class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        output = []
        source = [d[i] for i in digits]
        
        def dfs(i, path):
            if len(path) == len(digits):
                print(path)
                if path:
                    output.append(path)
                return
            
            for j in range(0, len(source[i])):
                print(source[i][j])
                dfs(i + 1, path + source[i][j])
            
        dfs(0, "")
        return output
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}
    
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            h1[s[i]] = 1 + h1.get(s[i], 0)

        for i in range(len(t)):
            if t[i] in h1 and h1[t[i]] > 0:
                h1[t[i]] -=1
            else:
                return False
        
        return True
        
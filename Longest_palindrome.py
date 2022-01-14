class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s[0]
        res = ''
        resLen = 0
        
        def check(l, r):
            nonlocal resLen, res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
                    
        for i in range(len(s)):
            
            check(i, i)
            check(i, i+1)
            
        return res
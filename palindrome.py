class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum())
        s = s.lower()
        
        l, r = 0, len(s)-1
        limit = len(s)//2
        
        while l< limit:
            if s[l] == s[r]:
                l +=1
                r -=1
            else:
                return False
        return True
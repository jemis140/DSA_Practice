#Most Frequent asked
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for i in s:
            
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if not stack:
                    return 
                else:
                    top = stack[-1]
                    if i == ')' and top == '(' or i == '}' and top == '{'  or i == ']' and top == '[':
                        stack.pop()
                    else:
                        return False
                                                                                   
        if not stack:
            return True
        
        else:
            return False
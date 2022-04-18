class Solution:
    def decodeString(self, s: str) -> str:
        #iterate thorugh string
        #if closing bracket then pop the item from character stack and number_stack and multiply character string with popped item which is number
             
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString    
            
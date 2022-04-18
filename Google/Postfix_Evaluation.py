class Solution:
    def cal(self,op1,op2,i):
        if i is "*":
            return op1 * op2
        elif i is "/":
            return int(op1 / op2)
        elif i is "+":
            return op1 + op2
        elif i is "-":
            return op1 - op2
        
    def evalRPN(self, tokens):
        operand = ["+", "-", "*", "/"]
        operand_stack = []
        for i in tokens:
            if i not in operand:
                operand_stack.append(int(i))
            else:
                num2= operand_stack.pop()
                num1 = operand_stack.pop()
                result = self.cal(num1, num2, i)
                operand_stack.append(result)
        return operand_stack.pop()

s = Solution()

input = ["2","1","+","3","*"]
result = s.evalRPN(input)
print(result)

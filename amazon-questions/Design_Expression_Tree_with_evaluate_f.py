# Given the postfix tokens of an arithmetic expression, build and return the binary expression tree that represents this expression.

# Postfix notation is a notation for writing arithmetic expressions in which the operands (numbers) appear before their operators. For example, the postfix tokens of the expression 4*(5-(7+2)) are represented in the array postfix = ["4","5","7","2","+","-","*"].

# its a property of postfix notation, the element to the left of the operator is always the right expression that needs to be evaluated first

# i.e
# take
# 32+
# in postfix the root is + then the first element to its right is 2. since 2 is a value we have reached a leaf node and know the next value after 2 is 3 which belongs to the left tree

import abc
from abc import ABC, abstractmethod
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""


class TreeNode:
    def __init__(self, value, op=None):
        self.left = None
        self.right = None
        self.op = op
        self.value = value

    def evaluate(self):
        if self.op == None:
            return int(self.value)

        if self.op == "+":
            return self.left.evaluate() + self.right.evaluate()

        if self.op == "-":
            return self.left.evaluate() - self.right.evaluate()

        if self.op == "*":
            return self.left.evaluate() * self.right.evaluate()

        if self.op == "/":
            return self.left.evaluate() // self.right.evaluate()


class TreeBuilder(object):
    def buildTree(self, postfix):
        stack = []

        ops = set(["+", "-", "/", "*"])

        for value in postfix:
            if value in ops:
                node = TreeNode(0, value)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
            else:
                stack.append(TreeNode(value))
        return stack[-1]


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""

class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

class Solution:

    def maxPathSum(self, root):
        res = [root.data]
        
        def dfs(root):
            
            if not root:
                return 0
            leftMax = dfs(root.left)
            leftMax = max(leftMax, 0)
            rightMax = dfs(root.right)
            rightMax = max(rightMax, 0)
            
            res[0] = max(res[0], root.data + leftMax + rightMax)
            
            return root.data + max(leftMax, rightMax)
        
        dfs(root)
        
        return res[0]

root = Node(-10)

root.insert(9)
root.insert(20)
root.insert(15)
root.insert(7)

s = Solution()

print(s.maxPathSum(root))
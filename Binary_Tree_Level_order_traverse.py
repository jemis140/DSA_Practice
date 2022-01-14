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
    def levelOrder(self, root):
        r = []
        q= []
        q.append(root)

        while q:

            # Dequeue a vertex from
            # queue and print it
            l = []
            qlen = len(q)
            for i in range(qlen):
                node = q.pop(0)

                if node:
                    l.append(node.data)
                    q.append(node.left)
                    q.append(node.right)

            if l:
                r.append(l)
        return r

root = Node(3)

root.insert(2)
root.insert(4)
root.insert(1)
root.insert(5)
root.insert(6)
root.insert(9)

s = Solution()

print(s.levelOrder(root))

            
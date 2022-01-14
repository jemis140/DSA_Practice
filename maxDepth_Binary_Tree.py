# Python3 program to find the maximum depth of tree

# A binary tree node
class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	# Compute the "maxDepth" of a tree -- the number of nodes
	# along the longest path from the root node down to the
	# farthest leaf node

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

	def maxDepth(self, node):
		if node is None:
			return 0 ;

		else :

			# Compute the depth of each subtree
			lDepth = self.maxDepth(node.left)
			rDepth = self.maxDepth(node.right)

			# Use the larger one
			if (lDepth > rDepth):
				return lDepth+1
			else:
				return rDepth+1


# Driver program to test above function
root = Node(1)
root.insert(2)
root.insert(3)

print ("Height of tree is %d" %(root.maxDepth(root)))


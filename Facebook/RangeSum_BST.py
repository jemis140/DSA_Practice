"""
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
"""
class Solution:
    
    def dfs(self, root: Optional[TreeNode], low: int, high: int ):
        if root:
            if root.val >= low and root.val <= high:
                self.res += root.val
            
            if root.val > low :
                self.dfs(root.left, low, high)

            if root.val < high:
                self.dfs(root.right, low, high)
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.res = 0
        
        self.dfs(root, low, high)
        
        return self.res
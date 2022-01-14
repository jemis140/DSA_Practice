class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        r = self.inorderTraversal(root)
        return r[k-1]
    
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res
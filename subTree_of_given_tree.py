class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return
        def check(r,s):
            if not s and not r:
                return True
            if not s or not r:
                return False
            if r.val == s.val and check(r.left, s.left) and check(r.right, s.right):
                return True
            else:
                return False
        if check(root,subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        else:
            return False
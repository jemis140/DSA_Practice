class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def find(n: TreeNode, val: int, path: List[str]) -> bool:
            if n.val == val:
                return True
            #recursively check val in left sub tree , if it's true then add "L" into path 
            if n.left and find(n.left, val, path):
                path += "L"
            #recursively check val in right sub tree , if it's true then add "R" into path 
            elif n.right and find(n.right, val, path):
                path += "R"
            return path
        # s represents path from source node to root and d represents destionation node to root
        s, d = [], []
        find(root, startValue, s)
        find(root, destValue, d)
        #removes common path until it's diffrent
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        # we traversed from source to root in a top to bottom manner so we will change all the path with "U" and for root -> destination 
        # we need to reverse path 
        return "".join("U" * len(s)) + "".join(reversed(d))

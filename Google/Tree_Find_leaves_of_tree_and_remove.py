class Solution:
    def findLeaves(self, root):
        #DFS check until node doesn't have children and add into list
        
        res = []
        def dfs(node):
            if not node:
                return -1
            h = max(dfs(node.left), dfs(node.right))+1
            if h >= len(res):
                res.append([])
            res[h].append(node.val)
            return h
        dfs(root)
        return res
        
s = Solution()
input = [1,2,3,4,5]
result = s.findLeaves(input)
print(result)
#Most Frequent Amazon Asked question
from collections import defaultdict
class Solution:
    def countComponents(self, n, edges):
        
        def dfsUtil(v,visited, graph):
            visited[v] = True
            
            for i in graph[v]:
                if visited[i] == False:
                    dfsUtil(i, visited, graph)            
        
        graph = defaultdict(list)

        for key, val in edges:
            graph[key].append(val)
            graph[val].append(key)
            
        visited = [False]*n
        
        count =0
        
        for i in range(n):
            if visited[i] == False:
                dfsUtil(i,visited, graph)
                count +=1
        return count

s = Solution()
edges = [[0,1], [1,2], [3,4]]
n = 5

print(s.countComponents(n, edges))
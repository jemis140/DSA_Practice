class Solution:
    def isCyclicUtil(self, v, visited, parent, graph):
        visited[v] = True
        
        for i in graph[v]:
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, v, graph) == True:
                    return True

            elif i != parent:
                return True
 
        return False
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = defaultdict(list)

        for key, val in edges:
            graph[key].append(val)
            graph[val].append(key)
            
        visited = [False]*n
        
        if len(edges) >= n:
            return False
        
        else:
            
            if self.isCyclicUtil(0, visited, -1, graph) == True:
                return False

            for i in range(n):
                if visited[i] == False:
                    return False
 
        return True
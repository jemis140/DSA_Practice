# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

# Solution: DFS, BFS, and UnionSet


class Solution:
    def findCircleNum(self, isConnected):
        visited = [0] * len(isConnected)
        count = 0

        def dfs(index):
            for connectedNodeIndex in range(0, len(isConnected)):
                if isConnected[index][connectedNodeIndex] == 1 and visited[connectedNodeIndex] == 0:
                    visited[connectedNodeIndex] = 1
                    dfs(connectedNodeIndex)
        for index, node in enumerate(isConnected):
            if visited[index] == 0:
                dfs(index)
                count += 1
        return count


class Solution:
    def findCircleNum(self, isConnected):
        visited = [0] * len(isConnected)
        count = 0
        queue = collections.deque([])
        for index, node in enumerate(isConnected):
            if visited[index] == 0:
                queue.append(index)
                while len(queue) > 0:
                    first = queue.popleft()
                    visited[first] = 1
                    for innerIndex in range(0, len(isConnected)):
                        if isConnected[index][innerIndex] == 1 and visited[innerIndex] == 0:
                            queue.append(innerIndex)
                count += 1
        return count

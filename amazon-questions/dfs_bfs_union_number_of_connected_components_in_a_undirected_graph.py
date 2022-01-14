# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

# Solution: DFS

class Solution:
    def countComponents(self, n: int, intervals: List[List[int]]) -> int:
        count = 0
        visited = set()
        intervals = sorted(intervals, key=lambda interval: (
            interval[0], interval[1]))
        hashmap = collections.defaultdict(list)

        for fromNode, toNode in intervals:
            hashmap[fromNode].append(toNode)
            hashmap[toNode].append(fromNode)

        def dfs(point):
            visited.add(point)
            for dest in hashmap[point]:
                if dest not in visited:
                    dfs(dest)

        for point in range(n):
            if point not in visited:
                dfs(point)
                count += 1

        return count


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry

        for x, y in edges:
            union(x, y)

        return len({find(i) for i in range(n)})


class Solution:
    def countComponents(self, n: int, intervals: List[List[int]]) -> int:
        count = 0
        visited = set()
        intervals = sorted(intervals, key=lambda interval: (
            interval[0], interval[1]))
        hashmap = collections.defaultdict(list)

        deq = deque()

        for fromNode, toNode in intervals:
            hashmap[fromNode].append(toNode)
            hashmap[toNode].append(fromNode)

        def bfs(node):
            deq = deque([node])
            while deq:
                newNode = deq.popleft()
                for nextNode in hashmap[newNode]:
                    if nextNode not in visited:
                        deq.append(nextNode)
                        visited.add(nextNode)

        for node in range(n):
            if node not in visited:
                visited.add(node)
                bfs(node)
                count += 1

        return count

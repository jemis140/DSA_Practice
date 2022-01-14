# There are n cities labeled from 1 to n. You are given the integer n and an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.

# Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1,

# The cost is the sum of the connections' costs used.

# Solution: Kruskal's Algorithm
# Greedy approach
# 1) Sort connections by minimum cost
# 2) Visit each connections check for loop, if not loop then add edge into tree
# 3) if edge are equal to the number of vertices, then return the cost
# 4) otherwise it's not possible

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections = sorted(connections, key=lambda connection: connection[2])
        parent = {city: city for city in range(1, n + 1)}
        ans = 0
        edges = []

        def find(city):
            if parent[city] != city:
                parent[city] = find(parent[city])
            return parent[city]

        def union(city1, city2):
            root1, root2 = find(city1), find(city2)
            if root1 == root2:
                return False
            parent[root2] = root1
            return True
        for city1, city2, cost in connections:
            if union(city1, city2):
                edges.append((city1, city2))
                ans += cost
        return ans if len(edges) == (n - 1) else -1

# Solution: Prim's Algorithm
# Greedy approach
# 1) For each city, find all the connections to the other city
# 2) Pick one arbitary node,
# 3) Pick the minimum cost of edge and non visited city
# 4) Add city to the visited, and update the queue with newly added city's connections
# 5) Repeat 3 and 4 untill the all the vertices are visited


class Solution:
    def minimumCost(self, n, connections):
        G = collections.defaultdict(list)
        for city1, city2, cost in connections:
            G[city1].append((cost, city2))
            G[city2].append((cost, city1))
        queue = [(0, 1)]
        visited = set()
        total = 0
        while queue and len(visited) < n:
            cost, city = heapq.heappop(queue)
            if city not in visited:
                visited.add(city)
                total += cost
                for edge_cost, next_city in G[city]:
                    heapq.heappush(queue, (edge_cost, next_city))
        return total if len(visited) == n else -1

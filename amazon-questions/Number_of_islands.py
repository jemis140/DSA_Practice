# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


import queue


class Solution:
    def numIslands(self, grid):
        totalRows = len(grid)
        totalColumns = len(grid[0])
        numberOfIsalands = 0

        def dfs(rowIndex, columnIndex):
            grid[rowIndex][columnIndex] = '0'
            if rowIndex - 1 >= 0 and grid[rowIndex - 1][columnIndex] == '1':
                dfs(rowIndex - 1, columnIndex)
            if columnIndex - 1 >= 0 and grid[rowIndex][columnIndex - 1] == '1':
                dfs(rowIndex, columnIndex - 1)
            if rowIndex + 1 < totalRows and grid[rowIndex + 1][columnIndex] == '1':
                dfs(rowIndex + 1, columnIndex)
            if columnIndex + 1 < totalColumns and grid[rowIndex][columnIndex + 1] == '1':
                dfs(rowIndex, columnIndex + 1)

        for rowIndex in range(0, totalRows):
            for columnIndex in range(0, totalColumns):
                if grid[rowIndex][columnIndex] == '1':
                    dfs(rowIndex, columnIndex)
                    numberOfIsalands += 1
        return numberOfIsalands

# Solution: BFS
# New Learning: Queue: https://docs.python.org/3/library/queue.html


class Solution:
    def numIslands(self, grid):
        totalRows = len(grid)
        totalColumns = len(grid[0])
        numberOfIsalands = 0

        for rowIndex in range(0, totalRows):
            for columnIndex in range(0, totalColumns):
                if grid[rowIndex][columnIndex] == '1':
                    neighbors = queue.Queue()
                    grid[rowIndex][columnIndex] == '0'
                    neighbors.put((rowIndex, columnIndex))
                    while neighbors.qsize() > 0:
                        ri, ci = neighbors.get()
                        if ri - 1 >= 0 and grid[ri - 1][ci] == '1':
                            neighbors.put((ri - 1, ci))
                            grid[ri - 1][ci] = '0'
                        if ci - 1 >= 0 and grid[ri][ci - 1] == '1':
                            neighbors.put((ri, ci - 1))
                            grid[ri][ci - 1] = '0'
                        if ri + 1 < totalRows and grid[ri + 1][ci] == '1':
                            neighbors.put((ri + 1, ci))
                            grid[ri + 1][ci] = '0'
                        if ci + 1 < totalColumns and grid[ri][ci + 1] == '1':
                            neighbors.put((ri, ci + 1))
                            grid[ri][ci + 1] = '0'
                    numberOfIsalands += 1
        return numberOfIsalands


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

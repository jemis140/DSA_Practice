# You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.
'''
w: BFS
h:  1) find the position of the person
    2) start from the position of the person, search all the possible positions
        then go the next 
    3) we only increase the count after 2)
'''


class Solution:
    def getFood(self, grid):
        totalRows = len(grid)
        totalColumns = len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        seen = set()

        for rowIndex in range(totalRows):
            for columnIndex in range(totalColumns):
                if grid[rowIndex][columnIndex] == '*':
                    start = (rowIndex, columnIndex)
                    break

        deq = deque([start])
        result = 0

        while deq:
            size = len(deq)

            for _ in range(size):
                cr, cc = deq.popleft()
                seen.add((cr, cc))

                if grid[cr][cc] == "#":
                    return result

                for dx, dy in directions:
                    newX = cr + dx
                    newY = cc + dy

                    if 0 <= newX < totalRows and 0 <= newY < totalColumns and grid[newX][newY] != "X" and (newX, newY) not in seen:
                        deq.append((newX, newY))
                        seen.add((newX, newY))
            result += 1
        return -1

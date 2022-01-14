# You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.

# You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the sticks until there is only one stick remaining.

# Return the minimum cost of connecting all the given sticks into one stick in this way.

# new learning: https://docs.python.org/3/library/heapq.html
import heapq


class Solution:
    def connectSticks(self, sticks):
        heapq.heapify(sticks)
        totalCost = 0
        while len(sticks) > 1:
            firstMinimum = heapq.heappop(sticks)
            secondMinimum = heapq.heappop(sticks)
            operationCost = firstMinimum + secondMinimum
            heapq.heappush(sticks, operationCost)
            totalCost += operationCost
        return totalCost

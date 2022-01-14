# Given two positive integers n and k.

# A factor of an integer n is defined as an integer i where n % i == 0.

# Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

# Solution: set + sort
import math


class Solution:
    def kthFactor(self, n, k):
        factors = set()
        factors.add(0)
        for number in range(1, math.floor(sqrt(n)) + 1):
            if n % number == 0:
                factors.add(number)
                if number != n // number:
                    factors.add(n // number)
        factors = sorted(factors)
        print(factors)
        return factors[k] if len(factors) > k else -1

# Solution: Heapq


class Solution:
    def kthFactor(self, n, k):
        heap = []

        def heappush_k(number):
            heapq.heappush(heap, number)
            if len(heap) > k:
                heapq.heappop(heap)
        for number in range(1, math.floor(sqrt(n)) + 1):
            if n % number == 0:
                heappush_k(-number)
                if number != n // number:
                    heappush_k(-(n // number))
        return -heapq.heappop(heap) if len(heap) == k else -1

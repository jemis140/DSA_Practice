# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

# For example, for arr = [2, 3, 4], the median is 3.
# For example, for arr = [2, 3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


from heapq import *


class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        heapq.heappush(self.maxHeap, -num)

        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        if len(self.maxHeap) < len(self.minHeap):
            num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -num)

    def findMedian(self):
        print(self.maxHeap, self.minHeap)
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2


class MedianFinder:

    def __init__(self):
        self.data = [], []

    def addNum(self, num: int) -> None:
        large, small = self.data

        if len(large) == len(small):
            heappush(large, -heappushpop(small, -num))
        else:
            heappush(small, -heappushpop(large, num))

    def findMedian(self) -> float:
        large, small = self.data
        if len(large) > len(small):
            return float(large[0])
        else:
            return float(large[0] - small[0])/2.0

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin(0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance(i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique(except for the order that it is in).

# Solution: find all distances sort them and return points

class Solution:
    def kClosest(self, points, k):
        minimum = 0
        distances = []
        for point in points:
            distance = sqrt(point[0]**2 + point[1]**2)
            distances.append((point[0], point[1], distance))
        distances = sorted(distances, key=lambda t: t[2])
        distances = list(map(lambda t: [t[0], t[1]], distances))
        return distances[:k]

# Solution: maxHeap


class Solution:
    def kClosest(self, points, k):
        maxHeap = []
        for point in points:
            distance = sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(maxHeap, (-distance, point))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [tuple[1] for tuple in maxHeap]

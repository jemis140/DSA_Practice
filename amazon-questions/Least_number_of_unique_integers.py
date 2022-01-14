# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        freqOfNumbers = Counter(arr)
        sortedNumber = sorted(arr, key=lambda number: (
            freqOfNumbers[number], number))
        print(sortedNumber)

        return len(set(sortedNumber[k:]))


# Trick: Counter.most_common() returns sorted order based on freq -> high to low
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        C = Counter(arr).most_common()
        res = len(C)
        for _, cnt in reversed(C):
            if cnt > k:
                break
            k -= cnt
            res -= 1
        return res


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        C = Counter(arr)
        sortedArray = sorted(C.values())
        res = len(C)
        for feq in sortedArray:
            if feq > k:
                break
            k -= feq
            res -= 1
        return res

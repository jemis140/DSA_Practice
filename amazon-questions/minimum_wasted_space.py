# You have n packages that you are trying to place in boxes, one package in each box. There are m suppliers that each produce boxes of different sizes (with infinite supply). A package can be placed in a box if the size of the package is less than or equal to the size of the box.

# The package sizes are given as an integer array packages, where packages[i] is the size of the ith package. The suppliers are given as a 2D integer array boxes, where boxes[j] is an array of box sizes that the jth supplier produces.

# You want to choose a single supplier and use boxes from them such that the total wasted space is minimized. For each package in a box, we define the space wasted to be size of the box - size of the package. The total wasted space is the sum of the space wasted in all the boxes.

# For example, if you have to fit packages with sizes [2,3,5] and the supplier offers boxes of sizes [4,8], you can fit the packages of size-2 and size-3 into two boxes of size-4 and the package with size-5 into a box of size-8. This would result in a waste of (4-2) + (4-3) + (8-5) = 6.
# Return the minimum total wasted space by choosing the box supplier optimally, or -1 if it is impossible to fit all the packages inside boxes. Since the answer may be large, return it modulo 109 + 7.

# New Learning: Binary Search

class Solution:
    def minWastedSpace(self, A, boxes):
        def binarySearch(arr, number):
            startPointer, endPointer = 0, len(arr)
            while startPointer < endPointer:
                mid = (startPointer + endPointer) // 2
                if arr[mid] <= number:
                    startPointer = mid + 1
                else:
                    endPointer = mid

            return startPointer

        A.sort()
        res = float("inf")
        for B in boxes:
            B.sort()
            if B[-1] < A[-1]:
                continue
            startIndex = 0
            curr = 0
            for b in B:
                j = binarySearch(A, b)
                curr += b * (j - startIndex)
                print(j, b, curr)
                startIndex = j
                print(res, curr)
            res = min(res, curr)
        return (res - sum(A)) % (10**9 + 7) if res < float("inf") else -1

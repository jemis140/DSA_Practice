# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log(m+n)).


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLength = (len(nums1) + len(nums2) + 1) // 2
        startIndex = 0
        endIndex = shortArray = len(nums1) if len(
            nums1) <= len(nums2) else len(nums2)

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        while startIndex <= endIndex:
            firstMid = (startIndex + endIndex) // 2
            secondMid = totalLength - firstMid

            if firstMid < shortArray and nums1[firstMid] < nums2[secondMid - 1]:
                startIndex = firstMid + 1
            elif firstMid > 0 and nums1[firstMid - 1] > nums2[secondMid]:
                endIndex = firstMid - 1
            else:

                if firstMid == 0:
                    leftMax = nums2[secondMid - 1]
                elif secondMid == 0:
                    leftMax = nums1[firstMid - 1]
                else:
                    leftMax = max(nums1[firstMid - 1], nums2[secondMid - 1])

                if (len(nums1) + len(nums2)) % 2 == 1:
                    return leftMax

                if firstMid == len(nums1):
                    rightMax = nums2[secondMid]
                elif secondMid == len(nums2):
                    rightMax = nums1[firstMid]
                else:
                    rightMax = min(nums1[firstMid], nums2[secondMid])

                return (leftMax + rightMax) / 2.0

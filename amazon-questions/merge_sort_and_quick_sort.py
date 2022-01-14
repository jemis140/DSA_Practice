class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) > 1:
                mid = len(nums) // 2

                left = nums[:mid]
                right = nums[mid:]

                mergeSort(left)
                mergeSort(right)

                i = j = k = 0

                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        nums[k] = left[i]
                        i += 1
                    else:
                        nums[k] = right[j]
                        j += 1
                    k += 1

                while i < len(left):
                    nums[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    nums[k] = right[j]
                    j += 1
                    k += 1

        mergeSort(nums)
        print(nums)


class Solution:
    def subarraysWithKDistinct(Self, A, K):
        def quickSort(arr):
            less = []
            equal = []
            greater = []

            if len(arr) > 1:
                pivot = arr[0]
                for i in arr:
                    if i < pivot:
                        less.append(i)
                    elif i == pivot:
                        equal.append(i)
                    elif i > pivot:
                        greater.append(i)

                return quickSort(less) + equal + quickSort(greater)
            else:
                return arr

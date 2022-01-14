class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        tracked = []
        for i, number in enumerate(nums):
            tracked.append([number, i])

        def merge(left, right):
            i = j = 0
            out = []

            numElemsRightArrayLessThanLeftArray = 0

            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    out.append(left[i])
                    res[left[i][1]] += numElemsRightArrayLessThanLeftArray
                    i += 1
                else:
                    # tracked[k][0] = right[j][0]
                    out.append(right[j])
                    numElemsRightArrayLessThanLeftArray += 1
                    j += 1

            while i < len(left):
                # tracked[k][0] = left[i][0]
                out.append(left[i])
                res[left[i][1]] += numElemsRightArrayLessThanLeftArray
                i += 1

            while j < len(right):
                # tracked[k] = right[j]
                out.append(right[j])
                j += 1

            return out

        def mergeSort(tracked):
            if len(tracked) == 1:
                return tracked
            mid = len(tracked) // 2

            left = tracked[:mid]
            right = tracked[mid:]

            left_r = mergeSort(left)
            right_r = mergeSort(right)
            return merge(left_r, right_r)

        mergeSort(tracked)

        return res

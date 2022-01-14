# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

# Algorithm
# initialize deque with first k elements
# 1) append the index of element if it's maximum than element in deque else break
# 2) perform this operation from kth element,
#  i) add deq[0] into the result as it's always first
#  ii) remove max elemenet if it's not in range of window
#  iii) append new element in deque follow 1)
# 3) add last window max to the result
class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        if k == 0:
            return nums

        deq = deque()
        result = []

        for i in range(k):
            while len(deq) != 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break

            deq.append(i)

        for i in range(k, len(nums)):
            result.append(nums[deq[0]])

            if deq[0] < i - k + 1:
                deq.popleft()

            while len(deq) != 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)

        result.append(nums[deq[0]])

        return result

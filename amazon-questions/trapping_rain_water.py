# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Solution: Dynamic Programming
class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)

        leftMax[0] = height[0]
        for index in range(1, len(height)):
            leftMax[index] = max(height[index], leftMax[index - 1])

        rightMax[-1] = height[-1]
        for index in range(len(height) - 2, -1, -1):
            rightMax[index] = max(height[index], rightMax[index + 1])

        ans = 0

        for index in range(1, len(height) - 1):
            ans += min(leftMax[index], rightMax[index]) - height[index]

        return ans

# Solution: Two Pointers


class Solution:
    def trap(self, height: List[int]) -> int:
        leftPointer = 0
        rightPointer = len(height) - 1
        leftMax = 0
        rightMax = 0
        ans = 0

        while leftPointer < rightPointer:
            if height[leftPointer] < height[rightPointer]:
                if height[leftPointer] >= leftMax:
                    leftMax = height[leftPointer]
                else:
                    ans += leftMax - height[leftPointer]
                leftPointer += 1
            else:
                if height[rightPointer] >= rightMax:
                    rightMax = height[rightPointer]
                else:
                    ans += rightMax - height[rightPointer]
                rightPointer -= 1
        return ans

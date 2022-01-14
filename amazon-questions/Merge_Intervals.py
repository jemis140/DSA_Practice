# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Solution: sort intervals based on start time, see if next interval can be merge into previous one or not
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval: interval[0])
        startTime = intervals[0][0]
        endTime = intervals[0][1]
        answer = []
        print(intervals)
        for interval in intervals[1:]:
            if startTime <= interval[0] <= endTime:
                endTime = max(endTime, interval[1])
            else:
                answer.append([startTime, endTime])
                startTime = interval[0]
                endTime = interval[1]
        answer.append([startTime, endTime])
        return answer

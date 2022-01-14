# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Solution: Heap

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        currentMeeting = []
        heapq.heappush(currentMeeting, intervals[0][1])
        for interval in intervals[1:]:
            if currentMeeting[0] <= interval[0]:
                heapq.heappop(currentMeeting)
            heapq.heappush(currentMeeting, interval[1])
        return len(currentMeeting)

# Solution: if start time is greater than the end time we don't need room and we can update end room time


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startTime = [interval[0] for interval in intervals]
        endTime = [interval[1] for interval in intervals]
        startTime = sorted(startTime)
        endTime = sorted(endTime)

        startPointer, endPointer, meetingRooms = 0, 0, 0

        while startPointer < len(startTime):
            if startTime[startPointer] >= endTime[endPointer]:
                endPointer += 1
            else:
                meetingRooms += 1
            startPointer += 1

        return meetingRooms

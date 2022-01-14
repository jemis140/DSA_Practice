# Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

# You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you can only attend one event at any time d.

# Return the maximum number of events you can attend.

# 1. Sort the events based on starting day of the event
# 2. Now once you have this sorted events, every day check what are the events that can start today
# 3. for all the events that can be started today, keep their ending time in heap.
# - Wait why we only need ending times ?
# i) from today onwards, we already know this event started in the past and all we need to know is when this event will finish
# ii) Also, another key to this algorithm is being greedy, meaning I want to pick the event which is going to end the soonest.
# - So how do we find the event which is going to end the soonest?
# i) brute force way would be to look at all the event's ending time and find the minimum, this is probably ok for 1 day but as we can only attend 1 event a day,
# we will end up repeating this for every day and that's why we can utilize heap(min heap to be precise) to solve the problem of finding the event with earliest ending time
# 4. There is one more house cleaning step, the event whose ending time is in the past, we no longer can attend those event
# 5. Last but very important step, Let's attend the event if any event to attend in the heap.

class Solution:
    def maxEvents(self, events):
        events = sorted(events, key=lambda event: event[0])
        maxDay = max([end for start, end in events])
        eventIndex = 0
        num_events_attended = 0

        minHeap = []

        for day in range(1, maxDay + 1):
            while eventIndex < len(events) and events[eventIndex][0] == day:
                heapq.heappush(minHeap, events[eventIndex][1])
                eventIndex += 1

            while minHeap and minHeap[0] < day:
                heapq.heappop(minHeap)

            if minHeap:
                heappop(minHeap)
                num_events_attended += 1
        return num_events_attended

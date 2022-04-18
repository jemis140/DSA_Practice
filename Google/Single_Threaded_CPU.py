"""Steps:

Sort the tasks according to start time, remember to keep a reference to the original task index
tasks = [[start_time, process_time, original_index], ..., ...]
Set the current time to the first start time in the task list.
Push all tasks whose start time is ≤ the current time into heap h.
heapq.heappush(h, (process_time, original_index))
Notice we don't care about start time, since we know any item pushed into
the heap is already past it's start_time.
Pop the first task to be processed.
Increase the current time by the processed time.
Repeat """

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        i = 0
        h = []
        time = tasks[0][0]
        while len(res) < len(tasks):
            while (i < len(tasks)) and (tasks[i][0] <= time):
                heapq.heappush(h, (tasks[i][1], tasks[i][2])) # (processing_time, original_index)
                i += 1
            if h:
                t_diff, original_index = heapq.heappop(h)
                time += t_diff
                res.append(original_index)
            elif i < len(tasks):
                time = tasks[i][0]
        return res
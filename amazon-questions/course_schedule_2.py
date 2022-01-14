# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair[0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.


class Solution:
    def findOrder(self, numCourses, prerequisites):
        courseDict = collections.defaultdict(list)
        indegree = {}

        if len(prerequisites) == 0:
            return [number for number in range(numCourses-1, -1, -1)]

        for course1, course2 in prerequisites:
            courseDict[course2].append(course1)

            indegree[course1] = indegree.get(course1, 0) + 1

        deq = deque([k for k in range(numCourses) if k not in indegree])

        result = []

        while deq:
            course = deq.popleft()
            result.append(course)

            if course in courseDict:
                for futureCourse in courseDict[course]:
                    indegree[futureCourse] -= 1

                    if indegree[futureCourse] == 0:
                        deq.append(futureCourse)

        return result if len(result) == numCourses else []

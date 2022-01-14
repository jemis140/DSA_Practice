# You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

# You have an array arr of length length with all zeros, and you have some operation to apply on arr. In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

# Return arr after applying all the updates.

# Solution 1: Brute Force : iterate all updates and update the array in ranges
# Solution 2: Update the array in range bases to perform the commulative sum later on
class Solution:
    def getModifiedArray(self, length, updates):
        result = [0]*length

        for update in updates:
            start, end, incr = update[0], update[1], update[2]
            result[start] += incr
            end += 1
            if end < length:
                result[end] -= incr

        for index in range(1, length):
            result[index] = result[index] + result[index - 1]

        return result

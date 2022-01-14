# Design and implement a data structure for a Least Frequently Used (LFU) cache.

# Implement the LFUCache class:

# LFUCache(int capacity) Initializes the object with the capacity of the data structure.
# int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
# void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
# To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

# When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

# The functions get and put must each run in O(1) average time complexity.

class Node:
    def __init__(self, key, value, count):
        self.key = key
        self.value = value
        self.count = count


class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.minCount = None
        self.key2node = {}
        self.count2node = collections.defaultdict(OrderedDict)

    def get(self, key):

        if key not in self.key2node:
            return -1

        return self.update(key)

    def update(self, key):
        node = self.key2node[key]
        del self.count2node[node.count][key]

        node.count += 1
        self.count2node[node.count][key] = node

        if not self.count2node[self.minCount]:
            self.minCount += 1

        return node.value

    def put(self, key, value):

        if not self.capacity:
            return

        if key in self.key2node:
            self.key2node[key].value = value
            self.update(key)
            return

        if len(self.key2node) == self.capacity:
            removedKey, removedValue = self.count2node[self.minCount].popitem(
                last=False)
            del self.key2node[removedKey]

        self.count2node[1][key] = self.key2node[key] = Node(key, value, 1)
        self.minCount = 1
        return

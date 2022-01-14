# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# new learning - orderedDict: https://docs.python.org/3/library/collections.html#collections.OrderedDict

from collections import OrderedDict


class LRUCache(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):

        if key in self:
            self.move_to_end(key)
        self[key] = value

        if len(self) > self.capacity:
            self.popitem(last=False)


class DoubleLinkedList():
    def __init__(self):  # init has def
        self.key = 0
        self.value = 0
        self.next = None
        self.prev = None


class LRUCache():
    def _add_node(self, node):
        node.prev = self.head  # head but from where
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        tail_node = self.tail.prev
        self._remove_node(tail_node)
        return tail_node

    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity

        self.head = DoubleLinkedList()
        self.tail = DoubleLinkedList()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        node = self.cache.get(key)

        if not node:
            newNode = DoubleLinkedList()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)
            self.size += 1

            if self.size > self.capacity:
                deletedNode = self._pop_tail()
                del self.cache[deletedNode.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)

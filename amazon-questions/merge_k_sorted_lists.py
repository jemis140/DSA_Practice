# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# new learning: merge two linked list

import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2List(l1, l2):
            head = ref = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    ref.next = l1
                    l1 = l1.next
                else:
                    ref.next = l2
                    l2 = l2.next
                ref = ref.next
            if not l1:
                ref.next = l2
            else:
                ref.next = l1

            return head.next

        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        prev = merge2List(lists[0], lists[1])

        for index in range(2, len(lists)):
            prev = merge2List(lists[index], prev)

        return prev


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = point = ListNode(0)
        heap = []

        for i, l in enumerate(lists):
            if l:
                heap.append((l.val, i, l))

        heapq.heapify(heap)

        while heap:
            val, index, node = heapq.heappop(heap)
            point.next = node
            point = point.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, index, node))

        return head.next

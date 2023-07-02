"""
A queue only supports enqueue and dequeue
Elements are added by being enqueued
Elements are removed by being dequeued
Tail is the most recently added(furthest) element
Head is the element about to come out
"""

import collections

class Queue:
    def __init__(self):
        self._data = collections.deque()
    
    def enqueue(self, x):
        self._data.append(x)
    
    def dequeue(self):
        return self._data.popleft()
    
    def max(self):
        return max(self._data)

# queues are great for when the order needs to be preserved 

# compute binary tree nodes in order of increasing depth

def binaryTreeDepthOrder(tree):
    result = []
    
    currentDepthNodes = [tree]
    while currentDepthNodes:
        result.append([curr.data for curr in currentDepthNodes])
        currentDepthNodes = [
            child for curr in currentDepthNodes for child in (curr.left, curr.right)
            if child
        ]
    return result


class CircularQueue:
    SCALE_FACTOR = 2

    def __init__(self,capacity):
        self._entries = [None] * capacity
        self._head = self._tail = self._numQueueOfElements = 0
    
    def enqueue(self, x):
        if self._numQueueOfElements == len(self._entries): # needs to resize
            self._entries = (
                self._entries[self._head:] + self._entries[:self._head])
            # resets head and tail
            self._head, self._tail = 0, self._numQueueOfElements
            self._entries += [None] * (
                len(self._entries) * CircularQueue.SCALE_FACTOR - len(self._entries)
            )
        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._numQueueOfElements += 1
    
    def dequeue(self):
        self._numQueueOfElements -= 1
        ret = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        return ret
    
    def size(self):
        return self._numQueueOfElements

# implement a queue using stacks

#!/usr/bin/env python3

class InitializedHeapError(Exception):
    def __init__(self,badHeap):
        self.message = "Heap must be initialized with an array of PriorityPair objects, was given: " + str(badHeap)

class PriorityPair:
    def __init__(self,priority,value):
        self.priority = priority
        self.value = value

    def __eq__(self,obj):
        return isinstance(obj,PriorityPair) and self.priority == obj.priority and self.value == obj.value

    def __repr__(self):
        return "PriorityPair: priority=" + str(self.priority) + " value=" + self.value.__repr__()

# min priority heap implementation that allows you to track objects with associated priorities
class MinPriorityHeap:
    def __init__(self,heap=None):
        if heap is not None and isinstance(heap,list) and any(map(lambda x: not isinstance(x,PriorityPair), heap)):
            raise InitializedHeapError(heap)
        self.heap = heap if heap is not None else list()

    def __eq__(self,obj):
        return isinstance(obj,MinPriorityHeap) and self.heap == obj.heap

    def __str__(self):
        return str(self.heap)

    def __repr__(self):
        return "MinPriorityHeap: heap=" + self.heap.__repr__()

    def peek(self):
        if len(self.heap)>0:
            return self.heap[0]
        return None

    # O( log(len(heap)) )
    def add(self,priority,value):
        priorityPair = PriorityPair(priority,value)
        self.heap.append(priorityPair)
        idx = len(self.heap)-1
        pIdx = parentIdx(idx)
        pPair = self.heap[pIdx]
        while pIdx >= 0 and pPair.priority > priorityPair.priority:
            self.heap[pIdx] = priorityPair
            self.heap[idx] = pPair
            idx = pIdx
            pIdx = parentIdx(idx)
            if pIdx >= 0:
                pPair = self.heap[pIdx]

    # m = len(values), O(m log(len(heap)))
    def addAll(self,priority,values):
        for value in values:
            self.add(priority,value)

    def remove(self,value):
        for idx,priorPair in enumerate(self.heap):
            if priorPair.value == value:
                self.heap[idx] = self.heap[len(self.heap)-1]
                self.heap = self.heap[:-1]
                self.minheapify(idx)
                return

    def pop(self):
        if len(self.heap) > 0:
            top = self.heap[0]
            self.heap[0] = self.heap[len(self.heap)-1]
            self.heap = self.heap[:-1]
            self.minheapify(0)
            return top.value
        else:
            return None

    def popWithPriority(self):
        if len(self.heap) > 0:
            top = self.heap[0]
            self.heap[0] = self.heap[len(self.heap)-1]
            self.heap = self.heap[:-1]
            self.minheapify(0)
            return top
        else:
            return None

    def minheapify(self,idx):
        lIdx = leftChildIdx(idx)
        rIdx = rightChildIdx(idx)
        if lIdx >= len(self.heap):
            return
        elif rIdx >= len(self.heap):
            curr = self.heap[idx]
            left = self.heap[lIdx]
            if left.priority < curr.priority:
                self.heap[idx] = left
                self.heap[lIdx] = curr
                self.minheapify(lIdx)
        else:
            curr = self.heap[idx]
            left = self.heap[lIdx]
            right = self.heap[rIdx]
            if left.priority < right.priority and left.priority < curr.priority:
                self.heap[idx] = left
                self.heap[lIdx] = curr
                self.minheapify(lIdx)
            elif left.priority >= right.priority and right.priority < curr.priority:
                self.heap[idx] = right
                self.heap[rIdx] = curr
                self.minheapify(rIdx)

    def isEmpty(self):
        return len(self.heap)==0

def parentIdx(i):
    return (i-1)//2

def leftChildIdx(i):
    return 2*i+1

def rightChildIdx(i):
    return 2*i+2
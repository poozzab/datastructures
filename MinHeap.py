#!/usr/bin/env python3

# Simple Min Heap implementation that works primarily with numeric values
class MinHeap:
    def __init__(self,heap=None):
        self.heap = heap if heap is not None else []

    def __eq__(self,obj):
        return isinstance(obj,MinHeap) and self.heap == obj.heap

    def __str__(self):
        return str(self.heap)

    def peek(self):
        if len(self.heap)>0:
            return self.heap[0]
        return None

    def add(self,value):
        self.heap.append(value)
        idx = len(self.heap)-1
        pIdx = parentIdx(idx)
        pVal = self.heap[pIdx]
        while pIdx >= 0 and pVal > value:
            self.heap[pIdx] = value
            self.heap[idx] = pVal
            idx = pIdx
            pIdx = parentIdx(idx)
            if pIdx >= 0:
                pVal = self.heap[pIdx]

    def remove(self,value):
        for idx,val in enumerate(self.heap):
            if val == value:
                self.heap[idx] = self.heap[len(self.heap)-1]
                self.heap = self.heap[:-1]
                self.minheapify(idx)

    def pop(self):
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
            if left < curr:
                self.heap[idx] = left
                self.heap[lIdx] = curr
                self.minheapify(lIdx)
        else:
            curr = self.heap[idx]
            left = self.heap[lIdx]
            right = self.heap[rIdx]
            if left < right and left < curr:
                self.heap[idx] = left
                self.heap[lIdx] = curr
                self.minheapify(lIdx)
            elif left >= right and right < curr:
                self.heap[idx] = right
                self.heap[rIdx] = curr
                self.minheapify(rIdx)

def parentIdx(i):
    return (i-1)//2

def leftChildIdx(i):
    return 2*i+1

def rightChildIdx(i):
    return 2*i+2
#!/usr/bin/env python3

class MinPriorQueue:
    def __init__(self):
        self.queue = []

    def clear(self):
        self.queue.clear()

    def add(self,prior,value):
        for idx,val in enumerate(self.queue):
            if prior <= val.priority:
                newQueue = self.queue[:idx]
                newQueue.append(Node(prior,value))
                newQueue.extend(self.queue[idx:])
                self.queue = newQueue
                return
        self.queue.append(Node(prior,value))

    # add an array of values that all have the same priority
    def addAll(self,prior,values):        
        for idx,val in enumerate(self.queue):
            if prior <= val.priority:
                newQueue = self.queue[:idx]
                newQueue.extend([Node(prior,value) for value in values])
                newQueue.extend(self.queue[idx:])
                self.queue = newQueue
                return
        self.queue.extend([Node(prior,value) for value in values])

    def pop(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0

    def __str__(self):
        res = "["
        for node in self.queue:
            res += node.__str__() + " "
        res += "]"
        return res

class Node:
    def __init__(self,prior,value):
        self.priority = prior
        self.value = value

    def __str__(self):
        return "p: " + str(self.priority) + " val: " + str(self.value)
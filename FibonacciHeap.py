#!/usr/bin/env python3

from DoubleLinkedList import DoubleLinkedList

class FibonacciHeap:
    def __init__(self):
        self.trees = DoubleLinkedList()
        self.min = None

    def __eq__(self,obj):
        return isinstance(obj,FibonacciHeap) and self.min == obj.min and self.trees == obj.trees

    def insert(self,value):
        newNode = self.trees.add(value)
        # self.min.value is expected to be a node in a tree
        # with a value property representing its key
        if self.min:
            if self.min.value.value > value:
                self.min = newNode
        else:
            self.min = newNode

    def quickInsert(self,value):
        self.trees.add(value)

    def deleteMin(self):
        children = self.min.value.children
        for child in children:
            self.quickInsert(child)
        self.trees.remove(self.min.value.value)
        self.updateMin()
        self.consolidateTrees()

    def consolidateTrees(self):
        rankDict = dict()
        currNode = self.trees.root
        while currNode:
            rank = currNode.value.rank
            if rank in rankDict:
                sameRankNode = rankDict.pop(rank)
                if currNode.value.value < sameRankNode.value.value:
                    currNode.value.addSubtree(sameRankNode.value)
                    self.trees.remove(sameRankNode.value.value)
                else:
                    sameRankNode.value.addSubtree(currNode.value)
                    currNode = self.trees.replaceWith(currNode.value,sameRankNode.value)
            else:
                rankDict[rank] = currNode
                currNode = currNode.next


    # O(n)
    def updateMin(self):
        if self.trees.isEmpty():
            return
        listNode = self.trees.root.next
        self.min = self.trees.root
        while listNode:
            if self.min.value.value > listNode.value.value:
                self.min = listNode
            listNode = listNode.next

    def __str__(self):
        return "FibHeap:[min:" + str(self.min.value.value) + " trees:" + str(self.trees) + "]"

class MinHeap:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else list()
        self.rank = len(children) if children is not None and isinstance(children,list) else 0
        self.marked = False

    def addSubtree(self,subTree):
        self.children.append(subTree)
        self.rank = len(self.children)

    def __eq__(self,obj):
        return isinstance(obj,MinHeap) and self.value == obj.value and self.children == obj.children and self.rank == obj.rank

    def __str__(self):
        return "Tree[v:{0}, r:{1}, {2}]".format(self.value,self.rank,str(self.children))

    def __repr__(self):
        return self.__str__()
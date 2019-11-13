#!/usr/bin/env python3

class DoubleLinkedList:
    def __init__(self):
        self.root = None
        self._itr = None

    def __eq__(self,obj):
        if isinstance(obj,DoubleLinkedList):
            leftNode = self.root
            rightNode = obj.root
            while leftNode and rightNode:
                if leftNode != rightNode:
                    return False
                leftNode = leftNode.next
                rightNode = rightNode.next
        else:
            return False
        # edge case: we were iterating and there are still nodes
        # left in one of the two DLLs
        if leftNode or rightNode:
            return False
        return True

    def __str__(self):
        res = "DLL: "
        node = self.root
        while node:
            res += str(node)
            if node.next:
                res += ", "
            node = node.next
        return res

    def add(self,value):
        if self.root:
            return self.root.add(value)
        else:
            self.root = DoubleLinkedNode(value,None)
            return self.root
            

    def remove(self,value):
        if self.root:
            self.root = self.root.remove(value)

    # remove the replacementValue node and put it in the spot of the replaceValue
    def replaceWith(self,replaceValue,replacementValue):
        replacementValueNode = None
        iterNode = self.root
        while iterNode and iterNode.value != replaceValue:
            if replacementValue == iterNode.value:
                replacementValueNode = iterNode
                if iterNode.next:
                    iterNode.next.prev = iterNode.prev
                if iterNode.prev:
                    iterNode.prev.next = iterNode.next
            iterNode = iterNode.next
        if iterNode:
            if replacementValueNode:
                if iterNode.prev:
                    iterNode.prev.next = replacementValueNode
                else:
                    self.root = replacementValueNode
                replacementValueNode.prev = iterNode.prev
                if iterNode.next:
                    iterNode.next.prev = replacementValueNode
                replacementValueNode.next = iterNode.next
        elif replacementValueNode:
            # failed to find the replaceValue node, but did find the replacementValueNode
            if replacementValueNode.prev:
                replacementValueNode.prev.next = replacementValueNode
            else:
                self.root = replacementValueNode
            if replacementValueNode.next:
                replacementValueNode.next.prev = replacementValueNode
        return replacementValueNode

    def isEmpty(self):
        return self.root is None

    def __iter__(self):
        self._itr = self.root
        return self

    def __next__(self):
        if self._itr is None:
            raise StopIteration
        node = self._itr
        self._itr = self._itr.next
        return node


class DoubleLinkedNode:
    def __init__(self,value,prev,nextNode=None):
        self.value = value
        self.prev = prev
        self.next = nextNode

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()

    def __eq__(self,obj):
        return isinstance(obj,DoubleLinkedNode) and self.value == obj.value

    def add(self,value):
        if self.next:
            return self.next.add(value)
        else:
            self.next = DoubleLinkedNode(value,self)
            return self.next

    def remove(self,value):
        if self.value.value == value:
            return self.next
        elif self.next:
            self.next = self.next.remove(value)
            if self.next:
                self.next.prev = self
        return self
#!/bin/python

from decimal import Decimal

# A balanced tree designed to handle quick addition and removal and median calculation
class AVL:
    def __init__(self,rootNode=None):
        self.root = rootNode

    def add(self,val):
        if self.root:
            self.root = self.root.add(val)
        else:
            self.root = Node(val)

    def remove(self,val,o):
        if self.root is not None:
            if not self.root.contains( val ):
                o.write("Wrong!\n")
            else:
                self.root = self.root.remove(val)
                if self.root is None:
                    o.write("Wrong!\n")
        elif self.root is None:
            o.write("Wrong!\n")

    def calculateRawMedian(self):
        if self.root:
            weights = self.root.getWeights()
            if weights[0] == weights[1]:
                return self.root.val
            elif weights[0] > weights[1]:
                leftLargest = self.root.left.findLargest()
                return ((self.root.val + leftLargest) / 2.0)
            else:
                rightSmallest = self.root.right.findSmallest()
                val = ((self.root.val + rightSmallest) / 2.0 )
                return val
        else:
            return None

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        # book keeping on height to reduce runtime complexity
        self.height = 0

    # mutate self to reflect the appropriate height
    # assumes child nodes are correct
    def adjustHeight(self):
        if self.left:
            lH = self.left.height
        else:
            lH = -1
        if self.right:
            rH = self.right.height
        else:
            rH = -1
        self.height = 1 + max(lH,rH)

    # must return the node rooted at the original location
    # in case it has changed
    def add(self,val):
        if self.val >= val:
            if self.left:
                self.left = self.left.add(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right = self.right.add(val)
            else:
                self.right = Node(val)
        self.adjustHeight()
        return self.checkbalance()

    # removes the first appearance of the value from the tree
    # returns the new root node
    def remove(self,val):
        if self.val == val:
            weights = self.getWeights()
            if self.left and weights[0] >= weights[1]:
                nextSmallestLargest = self.left.detachLargestDescFromRight(self)
                nextSmallestLargest.left = self.left
                nextSmallestLargest.right = self.right
                nextSmallestLargest.adjustHeight()
                return nextSmallestLargest.checkbalance()
            elif self.right:
                nextLargestSmallest = self.right.detachSmallestDescFromLeft(self)
                nextLargestSmallest.left = self.left
                nextLargestSmallest.right = self.right
                nextLargestSmallest.adjustHeight()
                return nextLargestSmallest.checkbalance()
            else:
                return None
        elif self.val > val:
            if self.left:
                self.left = self.left.remove(val)
                self.adjustHeight()
                return self.checkbalance()
            else:
                return self
        elif self.val < val:
            if self.right:
                self.right = self.right.remove(val)
                self.adjustHeight()
                return self.checkbalance()
            else:
                return self

    # check if value is contained within the AVL
    def contains(self,val):
        if self.val == val:
            return True
        elif self.left and self.val > val:
            return self.left.contains(val)
        elif self.right and self.val < val:
            return self.right.contains(val)
        else:
            return False

    # Search for the largest value in this subtree and return it
    def findLargest(self):
        if self.right:
            return self.right.findLargest()
        else:
            return self.val

    # search for the smallest value in this subtree and return it
    def findSmallest(self):
        if self.left:
            return self.left.findSmallest()
        else:
            return self.val

    # returns root node of subtree
    def checkbalance(self):
        diff = self.heightDiff()
        # if left - right > 1, too many on left
        if diff > 1:
            leftDiff = self.left.heightDiff()
            if leftDiff < 0:
                self.left = self.left.pivotLeft()
            return self.pivotRight()
        elif diff < -1:
            rightDiff = self.right.heightDiff()
            if rightDiff > 0:
                self.right = self.right.pivotRight()
            return self.pivotLeft()
        else:
            return self

    # returns a pair of numbers representing the left [0] and right [1] subtree weights
    # work weight into Node to reduce runtime complexity
    def getWeights(self):
        leftWeight = 0
        rightWeight = 0
        if self.left:
            leftWeight = self.left.getWeight()
        if self.right:
            rightWeight = self.right.getWeight()
        return (leftWeight, rightWeight)
    
    # singular method, returns total number of nodes in this subtree
    # work weight into Node to reduce runtime complexity
    def getWeight(self):
        weight = 1
        if self.left:
            weight += self.left.getWeight()
        if self.right:
            weight += self.right.getWeight()
        return weight

    # returns leftHeight - rightHeight
    def heightDiff(self):
        if self.left:
            lH = self.left.height
        else:
            lH = -1
        if self.right:
            rH = self.right.height
        else:
            rH = -1
        return lH - rH

    # perform node swapping, update heights, return new root
    def pivotLeft(self):
        right = self.right
        self.right = right.left
        right.left = self
        self.adjustHeight()
        right.adjustHeight()
        return right

    # perform node swapping, update height, return new root
    def pivotRight(self):
        left = self.left
        self.left = left.right
        left.right = self
        self.adjustHeight()
        left.adjustHeight()
        return left

    # call on child but provide self reference for update
    # indicate which direction the call is coming from for appropriate update
    def detachLargestDescFromRight(self,parent):
        if self.right:
            node = self.right.detachLargestDescFromLeft(self)
            self.adjustHeight()
            return node
        elif self.left:
            parent.left = self.left
        else:
            parent.left = None
        parent.adjustHeight()
        return self

    # call on child but provide self reference for update
    # indicate which direction the call is coming from for appropriate update
    def detachLargestDescFromLeft(self,parent):
        if self.right:
            node = self.right.detachLargestDescFromLeft(self)
            self.adjustHeight()
            return node
        elif self.left:
            parent.right = self.left
        else:
            parent.right = None
        parent.adjustHeight()
        return self

    # call on child but provide self reference for update
    # indicate which direction the call is coming from for appropriate update
    def detachSmallestDescFromLeft(self,parent):
        if self.left:
            node = self.left.detachSmallestDescFromRight(self)
            self.adjustHeight()
            return node
        elif self.right:
            parent.right = self.right
        else:
            parent.right = None
        parent.adjustHeight()
        return self

    # call on child but provide self reference for update
    # indicate which direction the call is coming from for appropriate update
    def detachSmallestDescFromRight(self,parent):
        if self.left:
            node = self.left.detachSmallestDescFromRight(self)
            self.adjustHeight()
            return node
        elif self.right:
            parent.left = self.right
        else:
            parent.left = None
        parent.adjustHeight()
        return self

def median(a,x,o):
    tree = AVL()
    for i in range(0,len(a)):
        if a[i] is 'a':
            tree.add(x[i])
        elif a[i] is 'r':
            tree.remove(x[i],o)

        median = Decimal(tree.calculateRawMedian())
        if median is not None:
            if median == median.to_integral():
                o.write(str(median.to_integral())+"\n")
            else:
                o.write(str(median)+"\n")

with open('testInput1.txt') as f:
    with open('testOutput1.txt','w') as o:
        N = int(f.readline())
        s = []
        x = []
        for i in range(0, N):
            tmp = f.readline().strip().split(' ')
            a, b = [xx for xx in tmp]
            s.append(a)
            x.append(int(b))
        median(s,x,o)
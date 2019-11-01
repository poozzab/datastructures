#!/usr/bin/env python3

# implement this
# originally had parameter name provided as "input"
# but I changed it to "string" because "input" is a keyword
# at the end, when asked if I was satisfied with this solution
# I said yes and acknowledge the extraneous variable of length
# but that I was happy with how everything was named
def isPalindrome(string):
    length = len(string)
    middle = length // 2
    endIdx = -1
    for idx in range(middle+1):
        if string[idx] != string[endIdx]:
            return False
        endIdx -= 1
    return True

# class and __init__ given
class ListNode:
    def __init__(self,value):
        self.value = value
        self.next = None

    # I decided to implement this to help with reverse
    def reverse(self,prev,head):
        if self.next == head:
            self.next = prev
            return self
        else:
            newHead = self.reverse(self,head)
            self.next = prev
            return newHead

# class, __init__, and signature of insert and reverse given
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # implement this
    # Q: is newNode an instance of the ListNode object?
    # A: Yes, newNode is an instance of ListNode
    def insert(self,newNode):
        node = self.head
        while node.next != self.head:
            node = node.next
        node.next = newNode
        newNode.next = self.head

    # implement this
    def reverse(self):
        newHead = self.head.reverse(self.head,self.head)
        self.head.next = newHead
        self.head = newHead
#!/usr/bin/env python3

import unittest
from CycleDetection import DTree, Node, Edge

class CycleDetection(unittest.TestCase):
    def test_hasCycle_doesHaveCycle_True(self):
        b = Node('b')
        abEdge = Edge(1,b)

        d = Node('d')
        cdEdge = Edge(3,d)

        c = Node('c',[cdEdge])
        acEdge = Edge(2,c)

        ecEdge = Edge(5,c)
        e = Node('e',[ecEdge])

        deEdge = Edge(4,e)
        d.addEdge(deEdge)

        a = Node('a', [abEdge, acEdge])

        tree = DTree(a)

        self.assertTrue(tree.hasCycle())


if __name__ == '__main__':
    unittest.main()
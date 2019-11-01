#!/usr/bin/env python3

import unittest
from DoubleLinkedList import DoubleLinkedList, DoubleLinkedNode

class DoubleLinkedListTest(unittest.TestCase):
    def test_replaceWith_replaceValueNotExist_doesNothing(self):
        dll = DoubleLinkedList()
        dll.add(1)
        node = dll.replaceWith(1,2)

        expectedDll = DoubleLinkedList()
        expectedDll.add(1)
        self.assertEqual(dll,expectedDll)
        self.assertIsNone(node)

    def test_replaceWith_replaceValueExistsReplacementValueDoesnt_doesNothing(self):
        dll = DoubleLinkedList()
        dll.add(1)
        dll.add(2)
        dll.add(3)

        node = dll.replaceWith(4,2)

        expectedDll = DoubleLinkedList()
        expectedDll.add(1)
        expectedDll.add(2)
        expectedDll.add(3)
        expectedNode = DoubleLinkedNode(2,None)

        self.assertEqual(dll,expectedDll)
        self.assertEqual(node,expectedNode)

    def test_replaceWith_bothExists_replacesValue(self):
        dll = DoubleLinkedList()
        dll.add(1)
        dll.add(2)
        dll.add(3)
        dll.add(4)

        node = dll.replaceWith(4,2)

        expectedDll = DoubleLinkedList()
        expectedDll.add(1)
        expectedDll.add(3)
        expectedDll.add(2)

        expectedNode = DoubleLinkedNode(2,None)

        self.assertEqual(dll,expectedDll)
        self.assertEqual(node,expectedNode)

    def test_iteration_canIterateMultipleTimes_iteratesFourTimesTwice(self):
        dll = DoubleLinkedList()
        dll.add(1)
        dll.add(2)
        dll.add(3)
        dll.add(4)
        count = 0
        for node in dll:
            count += 1
        self.assertEqual(count,4)
        count = 0
        for node in dll:
            count += 1
        self.assertEqual(count,4)

if __name__ == '__main__':
    unittest.main()
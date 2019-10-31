#!/usr/bin/env python3

import unittest
from FibonacciHeap import FibonacciHeap,MinHeap
from DoubleLinkedList import DoubleLinkedList, DoubleLinkedNode

class FibonacciHeapTest(unittest.TestCase):
    # testing situation explained in https://www.cs.princeton.edu/~wayne/teaching/fibonacci-heap.pdf
    def test_deleteMin_denseForest_successfullyConsolidates(self):
        seven = MinHeap(7,[MinHeap(30)])

        twentySix = MinHeap(26,[MinHeap(35)])
        twentyFour = MinHeap(24,[twentySix,MinHeap(46)])

        twentyThree = MinHeap(23)

        seventeen = MinHeap(17)

        eighteen = MinHeap(18,[MinHeap(39)])
        fiftyTwo = MinHeap(52)
        fortyOne = MinHeap(41,[MinHeap(44)])
        three = MinHeap(3,[eighteen,fiftyTwo,fortyOne])

        fibHeap = FibonacciHeap()
        fibHeap.quickInsert(seven)
        fibHeap.quickInsert(three)
        fibHeap.quickInsert(twentyThree)
        fibHeap.quickInsert(seventeen)
        fibHeap.quickInsert(twentyFour)
        fibHeap.updateMin()

        self.assertEqual(fibHeap.min.value,three)

        fibHeap.deleteMin()

        # setup expected heap
        twentySix = MinHeap(26,[MinHeap(35)])
        twentyFour = MinHeap(24,[twentySix,MinHeap(46)])

        seventeen = MinHeap(17,[MinHeap(23)])

        thirty = MinHeap(30)

        seven = MinHeap(7,[thirty,seventeen,twentyFour])

        fiftyTwo = MinHeap(52)

        fortyOne = MinHeap(41,[MinHeap(44)])
        eighteen = MinHeap(18,[MinHeap(39),fortyOne])
        expectedFibHeap = FibonacciHeap()
        expectedFibHeap.quickInsert(seven)
        expectedFibHeap.quickInsert(fiftyTwo)
        expectedFibHeap.quickInsert(eighteen)
        expectedFibHeap.updateMin()

        self.assertEqual(fibHeap,expectedFibHeap)
        
    def test_dllreplaceWith_replaceValueNotExist_doesNothing(self):
        dll = DoubleLinkedList()
        dll.add(1)
        node = dll.replaceWith(1,2)

        expectedDll = DoubleLinkedList()
        expectedDll.add(1)
        self.assertEqual(dll,expectedDll)
        self.assertIsNone(node)

    def test_dllreplaceWith_replaceValueExistsReplacementValueDoesnt_doesNothing(self):
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

    def test_dllreplaceWith_bothExists_replacesValue(self):
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

if __name__ == '__main__':
    unittest.main()
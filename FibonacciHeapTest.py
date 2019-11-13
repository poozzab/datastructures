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

    def test_consolidateTrees_twoNodesEqualRank_reparentsFirstNode(self):
        seven = MinHeap(7)
        three = MinHeap(3)

        actualHeap = FibonacciHeap()
        actualHeap.insert(seven)
        actualHeap.insert(three)

        expectedParentsBeforeConsolidate = {three: None, seven: None}

        self.assertEqual(expectedParentsBeforeConsolidate, actualHeap.parents)

        actualHeap.consolidateTrees()

        expectedParentsAfterConsolidate = {three: None, seven: three}
        self.assertEqual(actualHeap.parents, expectedParentsAfterConsolidate)

        threeThenSeven = MinHeap(3,[MinHeap(7)])
        expectedHeap = FibonacciHeap()
        expectedHeap.insert(threeThenSeven)

        self.assertEqual(actualHeap, expectedHeap)

if __name__ == '__main__':
    unittest.main()
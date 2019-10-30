#!/usr/bin/env python3

import unittest
from MinPriorityHeap import MinPriorityHeap, PriorityPair, InitializedHeapError

class MinHeapTest(unittest.TestCase):
    def test_add_emptyHeap_success(self):
        actualMinHeap = MinPriorityHeap()
        actualMinHeap.add(1,(0,0))
        
        expectedMinHeap = MinPriorityHeap([PriorityPair(1,(0,0))])
        self.assertEqual(actualMinHeap, expectedMinHeap)

    def test_add_nonEmptyHeap_addToEnd(self):
        actualMinHeap = MinPriorityHeap([PriorityPair(1,(0,0)),PriorityPair(2,(0,0)),PriorityPair(3,(0,0))])
        actualMinHeap.add(4,(0,0))

        expectedMinHeap = MinPriorityHeap([PriorityPair(1,(0,0)),PriorityPair(2,(0,0)),PriorityPair(3,(0,0)),PriorityPair(4,(0,0))])
        self.assertEqual(actualMinHeap, expectedMinHeap)

    def test_add_nonEmptyHeap_minheapifyOnce(self):
        actualMinHeap = MinPriorityHeap(convertToPriorityPairs([1,2,4,5,6]))
        actualMinHeap.add(3,(0,0))

        expectedMinHeap = MinPriorityHeap(convertToPriorityPairs([1,2,3,5,6,4]))
        self.assertEqual(actualMinHeap, expectedMinHeap)

    def test_add_multipleAdds_minheapifyToTop(self):
        actualMinHeap = MinPriorityHeap(convertToPriorityPairs([8,9,10,12,13,11]))
        # should append to end
        actualMinHeap.add(14, (0,0))
        # should rise to top
        actualMinHeap.add(1, (0,0))
        # should rise to second tier
        actualMinHeap.add(4, (0,0))

        expectedMinHeap = MinPriorityHeap(convertToPriorityPairs([1,4,10,8,13,11,14,12,9]))
        self.assertEqual(actualMinHeap, expectedMinHeap)

    def test_pop_emptyHeap_returnNone(self):
        actualMinHeap = MinPriorityHeap()
        actual = actualMinHeap.pop()

        self.assertIsNone(actual)

    def test_pop_singleElementHeap_returnsValueAndEmptiesHeap(self):
        actualMinHeap = MinPriorityHeap([PriorityPair(1,(0,0))])
        actualValue = actualMinHeap.pop()

        expectedValue = (0,0)
        self.assertEqual(actualValue,expectedValue)

        expectedMinHeap = MinPriorityHeap()
        self.assertEqual(actualMinHeap, expectedMinHeap)

    def test_pop_manyElementHeap_returnsValueAndRestructures(self):
        actualMinHeap = MinPriorityHeap(convertToPriorityPairs([1,2,4,5,6]))
        actualValue = actualMinHeap.pop()

        expectedValue = (0,0)
        self.assertEqual(actualValue,expectedValue)

        expectedMinHeap = MinPriorityHeap(convertToPriorityPairs([2,5,4,6]))
        self.assertEqual(actualMinHeap, expectedMinHeap)

    def test_remove_manyElementHeap_restructures(self):
        actualMinHeap = MinPriorityHeap(convertToPriorityPairs([8,PriorityPair(9,(1,1)),10,12,13,11,14]))
        actualMinHeap.remove((1,1))

        expectedMinHeap = MinPriorityHeap(convertToPriorityPairs([8,12,10,14,13,11]))
        self.assertEqual(actualMinHeap, expectedMinHeap)

    def test_remove_reqElementMissing_noop(self):
        actualMinHeap = MinPriorityHeap(convertToPriorityPairs([8,9,10,12,13,11,14]))
        actualMinHeap.remove(666)

        expectedMinHeap = MinPriorityHeap(convertToPriorityPairs([8,9,10,12,13,11,14]))
        self.assertEqual(actualMinHeap, expectedMinHeap)

    def test_minheapify_leftSmallest_swapWithLeft(self):
        actualMinHeap = MinPriorityHeap(convertToPriorityPairs([5,1,3]))
        actualMinHeap.minheapify(0)

        expectedMinHeap = MinPriorityHeap(convertToPriorityPairs([1,5,3]))
        self.assertEqual(actualMinHeap, expectedMinHeap)

    def test_minheapify_rootLargest_bubblesRootToBottom(self):
        actualMinHeap = MinPriorityHeap(convertToPriorityPairs([14,9,10,13,11,12]))
        actualMinHeap.minheapify(0)

        expectedMinHeap = MinPriorityHeap(convertToPriorityPairs([9,11,10,13,14,12]))
        self.assertEqual(actualMinHeap,expectedMinHeap)

    def test_init_initializedWithListOfIntegers_raisesException(self):
        self.assertRaises(InitializedHeapError, MinPriorityHeap, [1,2,3])

    def test_convertToPriorityPairs_allPriorityIntegers_success(self):
        array = [1,2,3]
        actual = convertToPriorityPairs(array)
        expected = [PriorityPair(1,(0,0)),PriorityPair(2,(0,0)),PriorityPair(3,(0,0))]
        self.assertEqual(actual,expected)

def convertToPriorityPairs(array):
    return list(map(lambda p: p if isinstance(p,PriorityPair) else PriorityPair(p,(0,0)),array))


if __name__ == '__main__':
    unittest.main()
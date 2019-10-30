#!/usr/bin/env python3

import unittest
from MinHeap import MinHeap

class MinHeapTest(unittest.TestCase):
    def test_add_emptyHeap_success(self):
        actualMinHeap = MinHeap()
        actualMinHeap.add(1)
        
        expectedMinHeap = MinHeap([1])
        self.assertEqual(actualMinHeap, expectedMinHeap)

    def test_add_nonEmptyHeap_addToEnd(self):
        actualMinHeap = MinHeap([1,2,3])
        actualMinHeap.add(4)

        expectedMinHeap = MinHeap([1,2,3,4])
        self.assertEqual(actualMinHeap, expectedMinHeap)

    def test_add_nonEmptyHeap_minheapifyOnce(self):
        actualMinHeap = MinHeap([1,2,4,5,6])
        actualMinHeap.add(3)

        expectedMinHeap = MinHeap([1,2,3,5,6,4])
        self.assertEqual(actualMinHeap, expectedMinHeap)

    def test_add_multipleAdds_minheapifyToTop(self):
        actualMinHeap = MinHeap([8,9,10,12,13,11])
        # should append to end
        actualMinHeap.add(14)
        # should rise to top
        actualMinHeap.add(1)
        # should rise to second tier
        actualMinHeap.add(4)

        expectedMinHeap = MinHeap([1,4,10,8,13,11,14,12,9])
        self.assertEqual(actualMinHeap, expectedMinHeap)

    def test_pop_emptyHeap_returnNone(self):
        actualMinHeap = MinHeap()
        actual = actualMinHeap.pop()

        self.assertIsNone(actual)

    def test_pop_singleElementHeap_emptiesHeap(self):
        actualMinHeap = MinHeap([1])
        actual = actualMinHeap.pop()

        self.assertEqual(actual,1)

        expectedMinHeap = MinHeap()
        self.assertEqual(actualMinHeap, expectedMinHeap)

    def test_pop_manyElementHeap_restructures(self):
        actualMinHeap = MinHeap([1,2,4,5,6])
        actualMinHeap.pop()

        expectedMinHeap = MinHeap([2,5,4,6])
        self.assertEqual(actualMinHeap, expectedMinHeap)

    def test_remove_manyElementHeap_restructures(self):
        actualMinHeap = MinHeap([8,9,10,12,13,11,14])
        actualMinHeap.remove(9)

        expectedMinHeap = MinHeap([8,12,10,14,13,11])
        self.assertEqual(actualMinHeap, expectedMinHeap)

    def test_remove_reqElementMissing_noop(self):
        actualMinHeap = MinHeap([8,9,10,12,13,11,14])
        actualMinHeap.remove(666)

        expectedMinHeap = MinHeap([8,9,10,12,13,11,14])
        self.assertEqual(actualMinHeap, expectedMinHeap)

    def test_minheapify_leftSmallest_swapWithLeft(self):
        actualMinHeap = MinHeap([5,1,3])
        actualMinHeap.minheapify(0)

        expectedMinHeap = MinHeap([1,5,3])
        self.assertEqual(actualMinHeap, expectedMinHeap)



if __name__ == '__main__':
    unittest.main()
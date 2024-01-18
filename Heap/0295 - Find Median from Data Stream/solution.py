from cgitb import small
import heapq
from operator import le


class MedianFinder:
    # Heap / Priority Queue implementation.

    def __init__(self):
        # Two Heaps -> maxHeap and minHeap.
        # Both Heaps should be equal size.
        self.maxHeap, self.minHeap = [], []

    # O(logn) to add to or remove from Heap.
    def addNum(self, num: int) -> None:
        # maxHeap is not implemented by default in Python.
        heapq.heappush(self.maxHeap, -1 * num)

        # Make sure every num in maxHeap is <= every num in minHeap.
        if (self.maxHeap and self.minHeap and (-1 * self.maxHeap[0]) > self.minHeap[0]):
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        # Check for uneven size between the two Heaps.
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * val)

    # O(1) to get min or max of Heap.
    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]

        return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2


if __name__ == '__main__':
    import unittest

    class Test(unittest.TestCase):

        def test_example_1(self):
            medianFinder = MedianFinder()
            medianFinder.addNum(1)
            medianFinder.addNum(2)
            medianFinder.findMedian()
            medianFinder.addNum(3)
            self.assertEqual(medianFinder.findMedian(), 2.0)

    unittest.main()

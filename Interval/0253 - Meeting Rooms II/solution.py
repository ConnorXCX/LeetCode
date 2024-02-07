from typing import List


class Solution:
    # Time Complexity:  O(nlogn) - need to sort intervals array.
    # Space Complexity: O(n) - need a start time array and end time array to get max overlaps.
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startTimes = sorted([interval[0] for interval in intervals])
        endTimes = sorted([interval[-1] for interval in intervals])

        count, maxCount, startPointer, endPointer = 0, 0, 0, 0

        while startPointer < len(intervals):
            if startTimes[startPointer] < endTimes[endPointer]:
                startPointer += 1
                count += 1
            else:
                endPointer += 1
                count -= 1

            maxCount = max(maxCount, count)

        return maxCount


if __name__ == '__main__':
    import unittest

    f = Solution().minMeetingRooms

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f([[0, 30], [5, 10], [15, 20]]), 2)

        def test_example_2(self):
            self.assertEqual(f([[7, 10], [2, 4]]), 1)

    unittest.main()

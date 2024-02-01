from typing import List


class Solution:
    # Time Complexity:  O(nlogn) - sorting and iterating input lists of intervals.
    # Space Complexity: TBD
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result, previousEnd = 0, intervals[0][1]

        for start, end in intervals[1:]:
            if start >= previousEnd:
                previousEnd = end
            else:
                result += 1
                previousEnd = min(end, previousEnd)

        return result


if __name__ == '__main__':
    import unittest

    f = Solution().eraseOverlapIntervals

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
            self.assertEqual(f([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)

        def test_example_2(self):
            # Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
            self.assertEqual(f([[1, 2], [1, 2], [1, 2]]), 2)

        def test_example_3(self):
            # Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
            self.assertEqual(f([[1, 2], [2, 3]]), 0)

    unittest.main()

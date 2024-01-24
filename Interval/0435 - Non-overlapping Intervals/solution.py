from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().eraseOverlapIntervals

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
            # Output: 1
            # Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
            self.assertEqual(f(), None)

        def test_example_2(self):
            # Input: intervals = [[1,2],[1,2],[1,2]]
            # Output: 2
            # Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
            self.assertEqual(f(), None)

        def test_example_3(self):
            # Input: intervals = [[1,2],[2,3]]
            # Output: 0
            # Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
            self.assertEqual(f(), None)

    unittest.main()

from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().merge

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
            # Output: [[1,6],[8,10],[15,18]]
            # Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
            self.assertEqual(f(), None)

        def test_example_2(self):
            # Input: intervals = [[1,4],[4,5]]
            # Output: [[1,5]]
            # Explanation: Intervals [1,4] and [4,5] are considered overlapping.
            self.assertEqual(f(), None)

    unittest.main()

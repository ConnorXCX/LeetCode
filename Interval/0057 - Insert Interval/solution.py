from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().insert

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
            # Output: [[1,5],[6,9]]
            self.assertEqual(f(), None)

        def test_example_2(self):
            # Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
            # Output: [[1,2],[3,10],[12,16]]
            # Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
            self.assertEqual(f(), None)

    unittest.main()

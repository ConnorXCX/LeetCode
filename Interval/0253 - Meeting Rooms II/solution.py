from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().minMeetingRooms

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f([[0, 30], [5, 10], [15, 20]]), 2)

        def test_example_2(self):
            self.assertEqual(f([[7, 10], [2, 4]]), 1)

    unittest.main()

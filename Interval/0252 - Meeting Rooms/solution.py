from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().canAttendMeetings

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f([[0, 30], [5, 10], [15, 20]]), False)

        def test_example_2(self):
            self.assertEqual(f([[7, 10], [2, 4]]), True)

    unittest.main()

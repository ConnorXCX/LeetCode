from typing import List


class Solution:
    # Time Complexity:  O(nlogn) - O(nlogn) to sort array based on start time and O(n) to iterate through sorted array; overall complexity is O(nlogn).
    # Space Complexity: TBD
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda i: i[0])

        for interval in range(1, len(intervals)):
            previousInterval = intervals[interval - 1]
            currentInterval = intervals[interval]

            if previousInterval[-1] > currentInterval[0]:
                return False

        return True


if __name__ == '__main__':
    import unittest

    f = Solution().canAttendMeetings

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f([[0, 30], [5, 10], [15, 20]]), False)

        def test_example_2(self):
            self.assertEqual(f([[7, 10], [2, 4]]), True)

    unittest.main()

from typing import List


class Solution:
    # Time Complexity:  O(nlogn) - sorting and iterating input lists of intervals.
    # Space Complexity: TBD
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            previousEnd = result[-1][1]

            if start <= previousEnd:
                result[-1][1] = max(previousEnd, end)
            else:
                result.append([start, end])

        return result


if __name__ == '__main__':
    import unittest

    f = Solution().merge

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
            self.assertEqual(f([[1, 3], [2, 6], [8, 10], [15, 18]]), [
                             [1, 6], [8, 10], [15, 18]])

        def test_example_2(self):
            # Explanation: Intervals [1,4] and [4,5] are considered overlapping.
            self.assertEqual(f([[1, 4], [4, 5]]), [[1, 5]])

    unittest.main()

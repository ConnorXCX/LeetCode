from typing import List


class Solution:
    # Time Complexity:  O(n) - iterating through list of intervals once since it is already sorted.
    # Space Complexity: O(n) - includes creation of result array.
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(
                    newInterval[1], intervals[i][1])]

        result.append(newInterval)

        return result


if __name__ == '__main__':
    import unittest

    f = Solution().insert

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])

        def test_example_2(self):
            # Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
            self.assertEqual(f([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]), [
                             [1, 2], [3, 10], [12, 16]])

    unittest.main()

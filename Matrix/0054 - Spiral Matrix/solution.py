from typing import List


class Solution:
    # Time Complexity:  O(mn) - iterating over matrix at least once.
    # Space Complexity: O(1) - in place operation, using four pointers / boundaries to track spiral position.
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)

        while left < right and top < bottom:
            # Get every value in top row.
            for i in range(left, right):
                result.append(matrix[top][i])

            # Shift top pointer / boundary down by one.
            top += 1

            # Get every value in right column.
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])

            # Shift right pointer / boundary left by one.
            right -= 1

            # Handle edge cases similar to 1 x 3 or 3 x 1 matrices, etc.
            if not (left < right and top < bottom):
                break

            # Get every value in bottom row.
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])

            # Shift bottom pointer / boundary up by one.
            bottom -= 1

            # Get every value in left column.
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])

            # Shift left pointer / boundary right by one.
            left += 1

        return result


if __name__ == '__main__':
    import unittest

    f = Solution().spiralOrder

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [
                             1, 2, 3, 6, 9, 8, 7, 4, 5])

        def test_example_2(self):
            self.assertEqual(f([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), [
                             1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])

    unittest.main()

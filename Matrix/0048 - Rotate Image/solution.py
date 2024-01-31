from typing import List


class Solution:
    # Time Complexity:  O(n^2) - iterating over matrix once.
    # Space Complexity: O(1) - in-place operation, using four pointers / boundaries to track rotations.
    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                # Same as left and right pointers / boundaries since given matrix is guaranteed to be n x n.
                top, bottom = left, right

                # Save top left value in temporary in-place variable.
                topLeft = matrix[top][left + i]

                # Move bottom left into top left.
                matrix[top][left + i] = matrix[bottom - i][left]

                # Move bottom right into bottom left.
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Move top right into bottom right.
                matrix[bottom][right - i] = matrix[top + i][right]

                # Move top left into top right.
                matrix[top + i][right] = topLeft

            # Shift right pointer / boundary left by one.
            right -= 1

            # Shift left pointer / boundary right by one.
            left += 1

        return matrix


if __name__ == '__main__':
    import unittest

    f = Solution().rotate

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [
                             [7, 4, 1], [8, 5, 2], [9, 6, 3]])

        def test_example_2(self):
            self.assertEqual(f([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]), [
                             [15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])

    unittest.main()

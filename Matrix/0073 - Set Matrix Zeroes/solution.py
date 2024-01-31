from typing import List


class Solution:
    # Time Complexity:  O(mn) - iterating over matrix at least once.
    # Space Complexity: O(1) - use top row and left column to track zeroing of rows and columns in place, use a variable to track overlap cell in top left corner.
    def setZeroes(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, columns = len(matrix), len(matrix[0])
        rowZero = False

        # Determine which rows and columns need to be zero.
        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # Zero the rows and columns based on the in place values in top row and left column, excluding value at matrix origin.
        for r in range(1, rows):
            for c in range(1, columns):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Zero the first column based on the in place value at matrix origin.
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # Zero the first row based on the in place value of rowZero variable.
        if rowZero:
            for c in range(columns):
                matrix[0][c] = 0

        return matrix


if __name__ == '__main__':
    import unittest

    f = Solution().setZeroes

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), [
                             [1, 0, 1], [0, 0, 0], [1, 0, 1]])

        def test_example_2(self):
            self.assertEqual(f([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]), [
                             [0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])

    unittest.main()

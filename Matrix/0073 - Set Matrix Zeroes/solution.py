from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


if __name__ == '__main__':
    import unittest

    f = Solution().setZeroes

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
            # Output: [[1,0,1],[0,0,0],[1,0,1]]
            self.assertEqual(f(), None)

        def test_example_2(self):
            # Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
            # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
            self.assertEqual(f(), None)

    unittest.main()

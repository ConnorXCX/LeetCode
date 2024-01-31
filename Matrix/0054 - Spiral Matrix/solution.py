from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass


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

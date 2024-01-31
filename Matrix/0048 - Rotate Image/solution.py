from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:



if __name__ == '__main__':
    import unittest

    f = Solution().rotate

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f([[1,2,3],[4,5,6],[7,8,9]]), [[7,4,1],[8,5,2],[9,6,3]])

        def test_example_2(self):
            self.assertEqual(f([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]), [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])

    unittest.main()

from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().pacificAtlantic

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
            # [0,4]: [0,4] -> Pacific Ocean
            #     [0,4] -> Atlantic Ocean
            # [1,3]: [1,3] -> [0,3] -> Pacific Ocean
            #     [1,3] -> [1,4] -> Atlantic Ocean
            # [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
            #     [1,4] -> Atlantic Ocean
            # [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
            #     [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
            # [3,0]: [3,0] -> Pacific Ocean
            #     [3,0] -> [4,0] -> Atlantic Ocean
            # [3,1]: [3,1] -> [3,0] -> Pacific Ocean
            #     [3,1] -> [4,1] -> Atlantic Ocean
            # [4,0]: [4,0] -> Pacific Ocean
            #     [4,0] -> Atlantic Ocean
            # Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
            self.assertEqual(f([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [
                             5, 1, 1, 2, 4]]), [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])

        def test_example_2(self):
            # Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
            self.assertEqual(f([[1]]), [[0, 0]])

    unittest.main()

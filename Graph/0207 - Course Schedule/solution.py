class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().canFinish

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: There are a total of 2 courses to take.
            # To take course 1 you should have finished course 0. So it is possible.
            self.assertEqual(f(2, [[1, 0]]), True)

        def test_example_2(self):
            # Explanation: There are a total of 2 courses to take.
            # To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
            self.assertEqual(f(2, [[1, 0], [0, 1]]), False)

    unittest.main()

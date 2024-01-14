class Solution:
    # Time Complexity:  O(n) - iterating through given array once.
    # Space Complexity: O(1) - no extra data structures required.
    def maxArea(self, height: list[int]) -> int:
        # Brute force implementation.
        # maxArea = 0

        # for l in range(len(height)):
        #     for r in range(l + 1, len(height)):
        #         currentArea = (r - l) * min(height[l], height[r])
        #         maxArea = max(maxArea, currentArea)

        # return maxArea

        # Optimized implementation.
        maxArea = 0
        l, r = 0, len(height) - 1

        while l < r:
            currentArea = (r - l) * min(height[l], height[r])
            maxArea = max(maxArea, currentArea)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxArea


if __name__ == '__main__':
    import unittest

    f = Solution().maxArea

    class Test(unittest.TestCase):

        def test_example_1(self):
            # The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
            self.assertEqual(f([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

        def test_example_2(self):
            self.assertEqual(f([1, 1]), 1)

    unittest.main()

class Solution:
    # Time Complexity:  O(n) - iterating through given array once.
    # Space Complexity: O(1) - no extra data structures required.
    def maxProduct(self, nums: list[int]) -> int:
        currentMin, currentMax = 1, 1
        maxSubArrayProduct = max(nums)

        for num in nums:
            previousMax = currentMax * num
            previousMin = currentMin * num
            currentMax = max(previousMax, previousMin, num)
            currentMin = min(previousMax, previousMin, num)
            maxSubArrayProduct = max(maxSubArrayProduct, currentMax)

        return maxSubArrayProduct


if __name__ == '__main__':
    import unittest

    f = Solution().maxProduct

    class Test(unittest.TestCase):

        def example_1(self):
            self.assertEqual(f([2, 3, -2, 4]), 6)

        def example_2(self):
            self.assertEqual(f([-2, 0, -1]), 0)

    unittest.main()

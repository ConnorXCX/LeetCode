class Solution:
    # Time Complexity:  O(n) - iterating through given array once.
    # Space Complexity: O(1) - no extra data structures required.
    def maxProduct(self, nums: list[int]) -> int:
        currentMin, currentMax = 1, 1
        maxSubArrayProduct = max(nums)

        for num in nums:
            tempMax = currentMax * num
            tempMin = currentMin * num
            currentMax = max(tempMax, tempMin, num)
            currentMin = min(tempMax, tempMin, num)
            maxSubArrayProduct = max(maxSubArrayProduct, currentMax)

        return maxSubArrayProduct


if __name__ == '__main__':
    import unittest

    f = Solution().maxProduct

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f([2, 3, -2, 4]), 6)

        def test_example_2(self):
            self.assertEqual(f([-2, 0, -1]), 0)

    unittest.main()

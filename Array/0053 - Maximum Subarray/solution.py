from typing import List


class Solution:
    # Time Complexity:  O(n) - iterate through array, removing any negative prefix while computing sum.
    # Space Complexity: O(1) - no extra data structures required.
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        maxSubArraySum = nums[0]

        for num in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += num
            maxSubArraySum = max(maxSubArraySum, currentSum)

        return maxSubArraySum


if __name__ == '__main__':
    import unittest

    f = Solution().maxSubArray

    class Test(unittest.TestCase):

        def test_example_1(self):
            # The subarray [4,-1,2,1] has the largest sum 6.
            self.assertEqual(f([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

        def test_example_2(self):
            # The subarray [1] has the largest sum 1.
            self.assertEqual(f([1]), 1)

        def test_example_3(self):
            # The subarray [5,4,-1,7,8] has the largest sum 23.
            self.assertEqual(f([5, 4, -1, 7, 8]), 23)

    unittest.main()

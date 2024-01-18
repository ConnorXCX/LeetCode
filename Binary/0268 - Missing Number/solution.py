from typing import List


class Solution:
    # Time Complexity:  O(n) - iterating through given array.
    # Space Complexity: O(1) - no extra data structures required.
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)

        for i in range(len(nums)):
            result += (i - nums[i])

        return result


if __name__ == '__main__':
    import unittest

    f = Solution().missingNumber

    class Test(unittest.TestCase):

        def test_example_1(self):
            # n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
            self.assertEqual(f([3, 0, 1]), 2)

        def test_example_2(self):
            # n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
            self.assertEqual(f([0, 1]), 2)

        def test_example_3(self):
            # n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
            self.assertEqual(f([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

    unittest.main()

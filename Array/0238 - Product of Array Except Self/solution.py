from typing import List


class Solution:
    # Time Complexity:  O(n) - using output array to track prefix and postfix array computations.
    # Space Complexity: O(1) - no extra data structures required.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = 1, 1
        answer = [1] * (len(nums))

        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer


if __name__ == '__main__':
    import unittest

    f = Solution().productExceptSelf

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f([1, 2, 3, 4]), [24, 12, 8, 6])

        def test_example_2(self):
            self.assertEqual(f([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    unittest.main()

class Solution:
    # Time Complexity:  O(logn) - required in problem statement.
    # Space Complexity: O(1) - no extra data structures required.
    def findMin(self, nums: list[int]) -> int:
        currentMinimum = nums[0]
        l, r = 0, len(nums) - 1

        # Implementation essentially involves a binary search algorithm.
        while l <= r:
            if nums[l] < nums[r]:
                currentMinimum = min(currentMinimum, nums[l])
                break

            m = (l + r) // 2
            currentMinimum = min(currentMinimum, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return currentMinimum


if __name__ == '__main__':
    import unittest

    f = Solution().findMin

    class Test(unittest.TestCase):

        def test_example_1(self):
            # The original array was [1,2,3,4,5] rotated 3 times.
            self.assertEqual(f([3, 4, 5, 1, 2]), 1)

        def test_example_2(self):
            # The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
            self.assertEqual(f([4, 5, 6, 7, 0, 1, 2]), 0)

        def test_example_3(self):
            # The original array was [11,13,15,17] and it was rotated 4 times.
            self.assertEqual(f([11, 13, 15, 17]), 11)

    unittest.main()

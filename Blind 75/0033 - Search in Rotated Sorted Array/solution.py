class Solution:
    # Time Complexity:  O(logn) - required in problem statement.
    # Space Complexity: O(1) - no extra data structures required.
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # Implementation essentially involves a binary search algorithm.
        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m

            # Left sorted portion.
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # Right sorted portion.
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1


if __name__ == '__main__':
    import unittest

    f = Solution().search

    class Test(unittest.TestCase):

        def example_1(self):
            self.assertEqual(f([4, 5, 6, 7, 0, 1, 2], 0), 4)

        def example_2(self):
            self.assertEqual(f([4, 5, 6, 7, 0, 1, 2], 3), -1)

        def example_3(self):
            self.assertEqual(f([1], 0), -1)

    unittest.main()

from typing import List


class Solution:
    # Time Complexity:  O(n) - iterating through array once and adding to hash map on each iteration (constant time operation).
    # Space Complexity: O(n) - could potentially add every value to hash map.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        return []


if __name__ == '__main__':
    import unittest

    f = Solution().twoSum

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Because nums[0] + nums[1] == 9, we return [0, 1].
            self.assertEqual(f([2, 7, 11, 15], 9), [0, 1])

        def test_example_2(self):
            self.assertEqual(f([3, 2, 4], 6), [1, 2])

        def test_example_3(self):
            self.assertEqual(f([3, 3], 6), [0, 1])

    unittest.main()

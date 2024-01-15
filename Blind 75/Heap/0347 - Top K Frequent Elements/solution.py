class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().topKFrequent

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f(), None)

        def test_example_2(self):
            self.assertEqual(f(), None)

    unittest.main()

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

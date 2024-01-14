class Solution:
    # Time Complexity:  O(nlogn) + O(n^2) -> O(n^2) - sorting array and then one loop to get initial value, and another loop to get essentially solve two sum.
    # Space Complexity: O(1) or O(n) depending on sorting implementation.
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()

        for i, value in enumerate(nums):
            if i > 0 and value == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = value + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    triplets.append([value, nums[l], nums[r]])
                    # Only need to update one pointer as conditions above will update the other pointer on next iteration.
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return triplets


if __name__ == '__main__':
    import unittest

    f = Solution().threeSum

    class Test(unittest.TestCase):

        def example_1(self):
            # nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
            # nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
            # nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
            # The distinct triplets are [-1,0,1] and [-1,-1,2].
            # Notice that the order of the output and the order of the triplets does not matter.
            self.assertEqual(f([-1, 0, 1, 2, -1, -4]),
                             [[-1, -1, 2], [-1, 0, 1]])

        def example_2(self):
            # The only possible triplet does not sum up to 0.
            self.assertEqual(f([0, 1, 1]), [])

        def example_3(self):
            # The only possible triplet sums up to 0.
            self.assertEqual(f([0, 0, 0]), [[0, 0, 0]])

    unittest.main()

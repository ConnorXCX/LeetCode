from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """


if __name__ == '__main__':
    import unittest

    f = Solution().reorderList

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Input: head = [1,2,3,4]
            # Output: [1,4,2,3]
            self.assertEqual(f(), None)

        def test_example_2(self):
            # Input: head = [1,2,3,4,5]
            # Output: [1,5,2,4,3]
            self.assertEqual(f(), None)

    unittest.main()

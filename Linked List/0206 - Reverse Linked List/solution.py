from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().reverseList

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Input: head = [1,2,3,4,5]
            # Output: [5,4,3,2,1]
            self.assertEqual(f(), None)

        def test_example_2(self):
            # Input: head = [1,2]
            # Output: [2,1]
            self.assertEqual(f(), None)

        def test_example_3(self):
            # Input: head = []
            # Output: []
            self.assertEqual(f(), None)

    unittest.main()

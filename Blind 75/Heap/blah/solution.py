from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().mergeKLists

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f(), None)

        def test_example_2(self):
            self.assertEqual(f(), None)

        def test_example_3(self):
            self.assertEqual(f(), None)

    unittest.main()

# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []

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
            # The linked-lists are:
            # [
            # 1->4->5,
            # 1->3->4,
            # 2->6
            # ]
            # merging them into one sorted list:
            # 1->1->2->3->4->4->5->6
            self.assertEqual(f([ListNode(1, ListNode(4, ListNode(5))),
                                ListNode(1, ListNode(3, ListNode(4))),
                                ListNode(2, ListNode(6))]), [
                1, 1, 2, 3, 4, 4, 5, 6])

        def test_example_2(self):
            self.assertEqual(f([]), [])

        def test_example_3(self):
            self.assertEqual(f([ListNode()]), [])

    unittest.main()

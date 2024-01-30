from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity:  O(n) - traversing Linked List once.
    # Space Complexity: O(n) - every node could potentially be stored in HashSet OR
    #                   O(1) - use two pointers.
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next

            if slow == fast:
                return True

        return False


if __name__ == '__main__':
    import unittest

    f = Solution().hasCycle

    class Test(unittest.TestCase):

        # https://stackoverflow.com/questions/66012561/about-leetcode-question-linked-list-cycle-python
        def getListNodes(self, values: list[int], pos: int) -> list[ListNode]:
            nodes = [ListNode(v) for v in values]

            for node, nextNode in zip(nodes, nodes[1:] + nodes[pos:pos + 1]):
                node.next = nextNode

            return nodes

        def test_example_1(self):
            # Input: head = [3,2,0,-4], pos = 1
            # Output: true
            # Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
            self.assertEqual(
                f(self.getListNodes([3, 2, 0, -4], 1)[0]), True)

        def test_example_2(self):
            # Input: head = [1,2], pos = 0
            # Output: true
            # Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
            self.assertEqual(
                f(self.getListNodes([1, 2], 0)[0]), True)

        def test_example_3(self):
            # Input: head = [1], pos = -1
            # Output: false
            # Explanation: There is no cycle in the linked list.
            self.assertEqual(f(self.getListNodes([1], -1)[0]), False)

    unittest.main()

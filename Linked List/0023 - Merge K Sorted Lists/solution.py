from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity:  O(nlogk) with logk being the number of times we have to split the k number of lists by 2, and do that n times, with n being the iterations through every node in list.
    # Space Complexity: TBD
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append((self.mergeTwoLists(list1, list2)))

            lists = mergedLists

        return lists[0]

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        initialNode = ListNode()
        currentNode = initialNode

        while list1 and list2:
            if list1.val < list2.val:
                currentNode.next = list1
                list1 = list1.next
            else:
                currentNode.next = list2
                list2 = list2.next

            currentNode = currentNode.next

        if list1:
            currentNode.next = list1
        elif list2:
            currentNode.next = list2

        return initialNode.next


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

            solutionList = []
            solutionListNodes = f([ListNode(1, ListNode(4, ListNode(5))),
                                   ListNode(1, ListNode(3, ListNode(4))),
                                   ListNode(2, ListNode(6))])

            while solutionListNodes:
                solutionList.append(solutionListNodes.val)
                solutionListNodes = solutionListNodes.next

            self.assertEqual(solutionList, [
                1, 1, 2, 3, 4, 4, 5, 6])

        def test_example_2(self):
            solutionList = []
            solutionListNodes = f([None])

            while solutionListNodes:
                solutionList.append(solutionListNodes.val)
                solutionListNodes = solutionListNodes.next

            self.assertEqual(solutionList, [])

        def test_example_3(self):
            solutionList = []
            solutionListNodes = f([])

            while solutionListNodes:
                solutionList.append(solutionListNodes.val)
                solutionListNodes = solutionListNodes.next

            self.assertEqual(solutionList, [])

    unittest.main()

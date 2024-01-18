from collections import deque
from typing import List, Optional
from unittest import result


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time Complexity:  O(n) - BFS implementation; visiting every node a single time.
    # Space Complexity: O(n) - Levels of a Binary Tree have max of n/2.
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = deque()
        q.append(root)

        while q:
            qLength = len(q)
            level = []

            for i in range(qLength):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)

        return res


if __name__ == '__main__':
    import unittest

    f = Solution().levelOrder

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f(TreeNode(3, TreeNode(9), TreeNode(
                20, TreeNode(15), TreeNode(7)))), [[3], [9, 20], [15, 7]])

        def test_example_2(self):
            self.assertEqual(f(TreeNode(1)), [[1]])

        def test_example_3(self):
            self.assertEqual(f(None), [])

    unittest.main()

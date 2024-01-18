from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time Complexity:  O(p + q) - iterating through every node.
    # Space Complexity: TBD
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS recursion implementation..

        # Both are empty trees.
        if not p and not q:
            return True

        # One empty tree; Not the same tree OR both are non-empty trees.
        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


if __name__ == '__main__':
    import unittest

    f = Solution().isSameTree

    # Function to get level order traversal of tree.
    def getLevelOrder(root: Optional[TreeNode]) -> List[int]:
        if root and root.val == 0 and root.left is None and root.right is None:
            return []

        while not root:
            return []

        queue = [root]
        result = []

        while queue:
            level_nodes = []
            temp = []
            for node in queue:
                level_nodes.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            result.append(level_nodes)

        return [item for items in result for item in items]

    class Test(unittest.TestCase):

        def test_example_1(self):
            # p = [1,2,3], q = [1,2,3]
            tree = TreeNode(1, TreeNode(2), TreeNode(3))
            self.assertEqual(f(tree, tree), True)

        def test_example_2(self):
            # p = [1,2], q = [1,null,2]
            p = TreeNode(1, TreeNode(2), None)
            q = TreeNode(1, None, TreeNode(2))
            self.assertEqual(f(p, q), False)

        def test_example_3(self):
            # p = [1,2,1], q = [1,1,2]
            p = TreeNode(1, TreeNode(2), TreeNode(1))
            q = TreeNode(1, TreeNode(1), TreeNode(2))
            self.assertEqual(f(p, q), False)

    unittest.main()

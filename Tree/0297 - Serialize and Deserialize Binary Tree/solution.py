from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    # Encodes a tree to a single string.
    # O(n) - DFS Preorder traversal implementation.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(node):
            if not node:
                result.append('N')
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ','.join(result)

    # Decodes your encoded data to tree.
    # O(n) - DFS Preorder traversal implementation.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(',')
        self.i = 0

        def dfs():
            if nodes[self.i] == 'N':
                self.i += 1
                return None

            node = TreeNode(int(nodes[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


if __name__ == '__main__':
    import unittest

    ser = Codec().serialize
    deser = Codec().deserialize

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(ser(TreeNode(1, TreeNode(2), TreeNode(
                3, TreeNode(4), TreeNode(5)))), '1,2,N,N,3,4,N,N,5,N,N')

        def test_example_2(self):
            self.assertEqual(ser(None), 'N')

        def test_example_3(self):
            deserTree = deser('1,2,N,N,3,4,N,N,5,N,N')
            self.assertEqual(deserTree.val, 1)
            self.assertEqual(deserTree.left.val, 2)
            self.assertEqual(deserTree.right.val, 3)
            self.assertEqual(deserTree.left.left, None)
            self.assertEqual(deserTree.left.right, None)
            self.assertEqual(deserTree.right.left.val, 4)
            self.assertEqual(deserTree.right.right.val, 5)
            self.assertEqual(deserTree.right.left.left, None)
            self.assertEqual(deserTree.right.left.right, None)
            self.assertEqual(deserTree.right.right.left, None)
            self.assertEqual(deserTree.right.right.right, None)

        def test_example_4(self):
            self.assertEqual(deser('N'), None)

    unittest.main()

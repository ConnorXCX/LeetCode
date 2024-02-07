from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def alienOrder(self, words: List[str]) -> str:
        # Topological Sort Implementation - DFS, but building result in reverse order.
        # Involves a Directed Acyclical Graph (DAG).
        # Post-Order Depth First Search traversal.
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ''

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {}
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True

            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ''

        res.reverse()

        return ''.join(res)


if __name__ == '__main__':
    import unittest

    f = Solution().alienOrder

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f(['wrt', 'wrf', 'er', 'ett', 'rftt']), 'wertf')

        def test_example_2(self):
            self.assertEqual(f(['z', 'x']), 'zx')

        def test_example_3(self):
            # Explanation: The order is invalid, so return ''.
            self.assertEqual(f(['z', 'x', 'z']), '')

    unittest.main()

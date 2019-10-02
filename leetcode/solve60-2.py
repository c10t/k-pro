import sys
import unittest
from typing import List

sys.setrecursionlimit(10 ** 6)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        c = sorted(candidates)
        solutions = []

        def backtrack(c, target, tree):
            # print(tree)
            if target == 0:
                solutions.append(tree)
                return

            for i, node in enumerate(c):
                if target < node:
                    break
                else:
                    backtrack(c[i:], target - node, tree + [node])

        backtrack(c, target, [])
        return solutions


class Test(unittest.TestCase):
    def setUp(self):
        self.solve = Solution()

    def test_CombinationSum(self):
        case = [
            ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
            ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ]
        for candidates, target, expected in case:
            answer = self.solve.combinationSum(candidates, target)
            self.assertCountEqual(answer, expected)


if __name__ == "__main__":
    unittest.main()

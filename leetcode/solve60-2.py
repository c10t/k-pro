import sys
import unittest
from typing import List
from itertools import permutations
from collections import defaultdict

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

    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)  # dict()
        for s in strs:
            key = "".join(sorted(s))
            answer[key].append(s)
            # if key in answer:
            #     answer[key].append(s)
            # else:
            #    answer[key] = [s]

        return answer.values()

    def myPow(self, x: float, n: int) -> float:
        # built-in
        # return x ** n

        # O(n)
        # p = 1
        # for _ in range(n):
        #   p *= x
        # return p

        m = abs(n)
        ans = 1.0
        while m:
            # print("--- step ---")
            # print(format(m, "b"))
            # print(format(m & 1, "b"))
            # print(ans)
            if m & 1:
                ans *= x
            x *= x
            m >>= 1

        return ans if n >= 0 else 1 / ans


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

    def test_Permutations(self):
        case = [
            (
                [1, 2, 3],
                [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)],
            )
        ]
        for nums, expected in case:
            answer = self.solve.permute(nums)
            self.assertCountEqual(answer, expected)

    def test_GroupAnagrams(self):
        case = [
            (
                ["eat", "tea", "tan", "ate", "nat", "bat"],
                [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
            )
        ]
        for strs, expected in case:
            answer = self.solve.groupAnagrams(strs)
            self.assertCountEqual(answer, expected)

    def test_PowXN(self):
        case = [(2.0, 10, 1024.0), (2.1, 3, 9.261), (2.0, -2, 0.25)]
        for x, n, expected in case:
            answer = self.solve.myPow(x, n)
            self.assertAlmostEqual(answer, expected)


if __name__ == "__main__":
    unittest.main()

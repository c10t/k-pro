import sys
import unittest
from typing import List
from itertools import accumulate, permutations
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

    # https://leetcode.com/problems/maximum-subarray/
    def maxSubArrayDP(self, nums: List[int]) -> int:
        # DP - O(n)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)

    def maxSubArrayDC(self, nums: List[int]) -> int:
        # Divide and Conquer - O(log n) ? but slow...
        return self.subProblem(nums, 0, len(nums) - 1)

    def subProblem(self, nums: List[int], lo: int, hi: int) -> int:
        # print(nums, lo, hi)
        mid = lo + (hi - lo) // 2

        if lo == hi:
            return nums[mid]

        l_max = self.subProblem(nums, lo, mid)
        r_max = self.subProblem(nums, mid + 1, hi)
        x_max = nums[mid]

        acc = x_max
        l, r = mid - 1, mid + 1

        # scan from middle to left
        while l >= lo:
            acc += nums[l]
            x_max = acc if acc > x_max else x_max
            l -= 1

        acc = x_max
        # scan from middle to rignt
        while r <= hi:
            acc += nums[r]
            x_max = acc if acc > x_max else x_max
            r += 1

        return max(x_max, l_max, r_max)

    def maxSubArrayIT(self, nums: List[int]) -> int:
        return max(accumulate(nums, lambda x, y: max(y, x + y)))

    def uniquePaths(self, m: int, n: int) -> int:
        return self.updp({}, m, n)

    def updp(self, dp: dict, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        elif m < 1 or n < 1:
            return 0
        elif (m, n) in dp:
            return dp[(m, n)]

        dp[(m, n)] = self.updp(dp, m - 1, n) + self.updp(dp, m, n - 1)
        return dp[(m, n)]


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

    def test_MaximumSubarray(self):
        case = [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)]
        for nums, expected in case:
            answer1 = self.solve.maxSubArrayDC(nums)
            answer2 = self.solve.maxSubArrayDP(nums)
            answer3 = self.solve.maxSubArrayIT(nums)
            self.assertEqual(answer1, expected)
            self.assertEqual(answer2, expected)
            self.assertEqual(answer3, expected)

    def test_UniquePaths(self):
        case = [(3, 2, 3), (7, 3, 28)]
        for m, n, expected in case:
            answer = self.solve.uniquePaths(m, n)
            self.assertEqual(answer, expected)


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List


class Solution:
    def q(self, nums: List[int], target: int) -> List[int]:
        raise NotImplementedError


class Test(unittest.TestCase):
    def setUp(self):
        self.solve = Solution()

    def test_q(self):
        inputs = [[2, 7, 11, 15], 9]
        answer = [0, 1]
        self.assertEqual(self.solve.q(*inputs), answer)


if __name__ == "__main__":
    unittest.main()

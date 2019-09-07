import unittest
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # https://leetcode.com/problems/two-sum/
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, v in enumerate(nums):
            d[v] = i

        for i, v in enumerate(nums):
            candidate = target - v
            if candidate in d.keys() and d[candidate] != i:
                return [i, d[candidate]]

    # https://leetcode.com/problems/add-two-numbers/
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        q = 0
        root = node = ListNode(0)
        v1 = l1
        v2 = l2
        while v1 or v2 or q:
            x = y = 0
            if v1:
                x = v1.val
                v1 = v1.next
            if v2:
                y = v2.val
                v2 = v2.next
            q, mod = divmod(x + y + q, 10)
            node.next = ListNode(mod)
            node = node.next

        return root.next

    # https://leetcode.com/problems/longest-substring-without-repeating-characters/
    def lengthOfLongestSubstring(self, s: str) -> int:
        candidate = {}
        memo = {}
        substr = ''
        for i, char in enumerate(s):
            # print('---')
            # print(substr)
            # print(memo)
            if char in memo:
                candidate[substr] = len(substr)
                substr = s[memo[char] + 1 : i]
                memo = {char: memo[char] for char in substr}

            memo[char] = i
            substr += char

        candidate[substr] = len(substr)
        # print(candidate)
        return max(candidate.values())


class Test(unittest.TestCase):
    def setUp(self):
        self.solve = Solution()

    def test_TwoSum_ExampleCase(self):
        inputs = [[2, 7, 11, 15], 9]
        answer = [0, 1]
        self.assertEqual(self.solve.twoSum(*inputs), answer)

    def test_AddTwoNumbers_ExampleCase(self):
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0

        def tolist(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = tolist(n // 10)
            return node

        def addTwoNumbers(l1, l2):
            return tolist(toint(l1) + toint(l2))
        l1, l2 = (342, 465)
        answer = 807
        submission = self.solve.addTwoNumbers(tolist(l1), tolist(l2))
        self.assertEqual(toint(submission), answer)

    def test_LongestSubstringWithoutRepeatingChars_ExampleCase(self):
        case = [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ("dvdf", 3)]
        for s, answer in case:
            self.assertEqual(self.solve.lengthOfLongestSubstring(s), answer)


if __name__ == "__main__":
    unittest.main()

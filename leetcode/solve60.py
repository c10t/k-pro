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

    # https://leetcode.com/problems/zigzag-conversion/
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        if numRows == 2:
            even = ''.join([char for i, char in enumerate(s) if i % 2 == 0])
            oddd = ''.join([char for i, char in enumerate(s) if i % 2 == 1])
            return even + oddd
        nmat = [['' for _ in range(len(s))] for _ in range(numRows)]
        divider = numRows + (numRows - 2)

        for i, char in enumerate(s):
            quot, reminder = divmod(i, divider)
            if reminder < numRows:
                # print(quot, reminder)
                nmat[reminder][quot + (numRows - 2) * quot] = char
            else:
                col = numRows - 2 - reminder + numRows
                row = quot + (numRows - 2) * quot + numRows - 1 - col
                nmat[col][row] = char

        answer = ''
        for line in nmat:
            # print(line)
            answer += ''.join(line)

        return answer

    def myAtoi(self, st: str) -> int:
        s = st.strip()
        decimal = '0123456789'
        value = ''
        sign = 1
        for i, char in enumerate(s):

            if (char != '+' and char != '-') and char not in decimal:
                break
            if (char == '+' or char == '-') and i > 0:
                # print('here1')
                break
            if (char == '+' or char == '-') and i == 0:
                # print('here')
                sign = -1 if char == '-' else 1
                continue
            value += char

        if len(value) < 1:
            return 0

        answer = sign * int(value)

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        if answer < INT_MIN:
            return INT_MIN

        if answer > INT_MAX:
            return INT_MAX

        return answer

    def isValid(self, s: str) -> bool:
        stack = []
        for char in reversed(s):
            # print(char)
            stack_remain = len(stack) > 0
            closed_parenthesis = char in ['(', '[', '{']
            if not stack_remain and closed_parenthesis:
                # print('NG')
                return False
            if not stack_remain and not closed_parenthesis:
                # print('stacking F')
                stack.append(char)
                continue
            if stack_remain and not closed_parenthesis:
                # print('stacking C')
                stack.append(char)
                continue
            if stack_remain and closed_parenthesis:
                last = stack.pop()
                # print('pop:', last)
                if char == '(' and last == ')':
                    # print('()')
                    continue
                if char == '[' and last == ']':
                    # print('[]')
                    continue
                if char == '{' and last == '}':
                    # print('{}')
                    continue
                # print('here')
                return False

        return False if len(stack) > 0 else True


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

    def test_ZigZagConversion_ExampleCase(self):
        case = [
            ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
            ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
            ("A", 1, "A")
        ]
        for s, numRows, answer in case:
            self.assertEqual(self.solve.convert(s, numRows), answer)

    def test_MyAtoI_ExampleCase(self):
        case = [
            ("42", 42), ("   -42", -42), ("+1", 1), ("++1", 0),
            ("4193 with words", 4193), ("words and 987", 0),
            ("-91283472332", -2147483648), ("0-1", 0)
        ]
        for s, answer in case:
            self.assertEqual(self.solve.myAtoi(s), answer)

    def test_IsValidParenthesis_ExampleCase(self):
        case = [
            ("()", True), ("()[]{}", True), ("(]", False),
            ("([)]", False), ("{[]}", True), ("}", False)
        ]
        for s, answer in case:
            self.assertEqual(self.solve.isValid(s), answer)


if __name__ == "__main__":
    unittest.main()

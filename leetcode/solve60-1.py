import unittest
from typing import List
from bisect import bisect_left, bisect_right


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
        substr = ""
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
            even = "".join([char for i, char in enumerate(s) if i % 2 == 0])
            oddd = "".join([char for i, char in enumerate(s) if i % 2 == 1])
            return even + oddd
        nmat = [["" for _ in range(len(s))] for _ in range(numRows)]
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

        answer = ""
        for line in nmat:
            # print(line)
            answer += "".join(line)

        return answer

    # https://leetcode.com/problems/string-to-integer-atoi
    def myAtoi(self, st: str) -> int:
        s = st.strip()
        decimal = "0123456789"
        value = ""
        sign = 1
        for i, char in enumerate(s):

            if (char != "+" and char != "-") and char not in decimal:
                break
            if (char == "+" or char == "-") and i > 0:
                # print('here1')
                break
            if (char == "+" or char == "-") and i == 0:
                # print('here')
                sign = -1 if char == "-" else 1
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

    # https://leetcode.com/problems/valid-parentheses
    def isValid(self, s: str) -> bool:
        stack = []
        for char in reversed(s):
            # print(char)
            stack_remain = len(stack) > 0
            closed_parenthesis = char in ["(", "[", "{"]
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
                if char == "(" and last == ")":
                    # print('()')
                    continue
                if char == "[" and last == "]":
                    # print('[]')
                    continue
                if char == "{" and last == "}":
                    # print('{}')
                    continue
                # print('here')
                return False

        return False if len(stack) > 0 else True

    # https://leetcode.com/problems/generate-parentheses
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        else:
            return self.helper([""], n, 0)

    def helper(self, container, m, num_closes):
        # print('m={0}, num_closes={1}'.format(m, num_closes))
        # print(container)
        if m == 0:
            return [s + ")" * num_closes for s in container]
        if num_closes == 0:
            return self.helper([s + "(" for s in container], m - 1, num_closes + 1)
        else:
            return self.helper(
                [s + "(" for s in container], m - 1, num_closes + 1
            ) + self.helper([s + ")" for s in container], m, num_closes - 1)

    # https://leetcode.com/problems/next-permutation
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return

        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i < 1:
            nums.reverse()
            return
        else:
            nums[i:] = nums[: i - 1 : -1]
            j = bisect_right(nums, nums[i - 1], i)
            nums[j], nums[i - 1] = nums[i - 1], nums[j]

    # https://leetcode.com/problems/search-in-rotated-sorted-array
    def search_in_rotated(self, nums: List[int], target: int) -> int:
        l = len(nums)  # O(1)
        if l < 1:
            return -1

        b = [0, l]
        while b[0] != b[1]:  # O(log n)?
            # print(b)
            mean = (b[0] + b[1]) // 2
            i, j = b[0], b[1]
            if nums[mean] - nums[i] > 0:
                b = [mean, j]
            else:
                b = [i, mean]
        # print(b)

        if nums[(i + 1) % l] - nums[i] < 0:
            i = (i + 1) % l

        idx = bisect_left(nums[i:l] + nums[0:i], target) + i  # O(log n)?
        idx %= l
        return idx if nums[idx] == target else -1

    # https://leetcode.com/problems/search-insert-position
    def search_insert(self, nums: List[int], target: int) -> int:
        idx = bisect_left(nums, target)
        return idx


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
            ("A", 1, "A"),
        ]
        for s, numRows, answer in case:
            self.assertEqual(self.solve.convert(s, numRows), answer)

    def test_MyAtoI_ExampleCase(self):
        case = [
            ("42", 42),
            ("   -42", -42),
            ("+1", 1),
            ("++1", 0),
            ("4193 with words", 4193),
            ("words and 987", 0),
            ("-91283472332", -2147483648),
            ("0-1", 0),
        ]
        for s, answer in case:
            self.assertEqual(self.solve.myAtoi(s), answer)

    def test_IsValidParenthesis_ExampleCase(self):
        case = [
            ("()", True),
            ("()[]{}", True),
            ("(]", False),
            ("([)]", False),
            ("{[]}", True),
            ("}", False),
        ]
        for s, answer in case:
            self.assertEqual(self.solve.isValid(s), answer)

    def test_GenerateParentheses_ExampleCase(self):
        case = [(3, ["((()))", "(()())", "(())()", "()(())", "()()()"])]
        for num, answer in case:
            self.assertCountEqual(self.solve.generateParenthesis(num), answer)

    def test_NextPermutation_ExampleCase(self):
        case = [
            ([1, 2, 3], [1, 3, 2]),
            ([3, 2, 1], [1, 2, 3]),
            ([1, 1, 5], [1, 5, 1]),
            ([1, 3, 2], [2, 1, 3]),
        ]
        for i, o in case:
            self.solve.nextPermutation(i)  # destructive!
            self.assertSequenceEqual(i, o)

    def test_SearchInRotatedSortedArray_ExampleCase(self):
        case = [([4, 5, 6, 7, 0, 1, 2], 0, 4), ([4, 5, 6, 7, 0, 1, 2], 3, -1)]
        for nums, target, expected in case:
            output = self.solve.search_in_rotated(nums, target)
            self.assertEqual(output, expected)

    def test_SearchInsertPosition_ExampleCase(self):
        case = [
            ([1, 3, 5, 6], 5, 2),
            ([1, 3, 5, 6], 2, 1),
            ([1, 3, 5, 6], 7, 4),
            ([1, 3, 5, 6], 0, 0),
        ]
        for nums, target, expected in case:
            output = self.solve.search_insert(nums, target)
            self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()

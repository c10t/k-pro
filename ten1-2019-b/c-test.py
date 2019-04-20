import unittest

# https://atcoder.jp/contests/tenka1-2019-beginner/tasks_print


def count(s):
    w = s.count('.')
    candidate = w
    for i in range(len(s)):
        if s[i] == '#':
            w += 1
        else:
            w -= 1
        candidate = min(candidate, w)

    return candidate


class Test(unittest.TestCase):
    data = [
        ('#.#', 1), ('#.##.', 2), ('.........', 0)
    ]
    data4 = [
        ('....', 0), ('...#', 0), ('..#.', 1), ('..##', 0),
        ('.#..', 1), ('.#.#', 1), ('.##.', 1), ('.###', 0),
        ('#...', 1), ('#..#', 1), ('#.#.', 2), ('#.##', 1),
        ('##..', 2), ('##.#', 1), ('###.', 1), ('####', 0),
    ]
    data5 = [
        ('.', 0), ('#', 0), ('.' * (2 * (10 ** 5)), 0),
        ('#...#', 1), ('#....#', 1), ('.#..#.', 2),
        ('..#..##', 1), ('..##.##', 1), ('..##..#', 2),
        ('...###...', 3)
    ]
    data7 = [
        ('..#..##..#.', 4)
    ]

    def test_given(self):
        for test in self.data:
            actual = count(test[0])
            msg = 'test target: {}'.format(test[0])
            self.assertEqual(actual, test[1], msg)

    # @unittest.skip('')
    def test_all4(self):
        for test in self.data4:
            actual = count(test[0])
            msg = 'test target: {}'.format(test[0])
            self.assertEqual(actual, test[1], msg)

    # @unittest.skip('')
    def test_additional(self):
        for test in self.data5:
            actual = count(test[0])
            msg = 'test target: {}'.format(test[0])
            self.assertEqual(actual, test[1], msg)

    def test_standart(self):
        for test in self.data7:
            actual = count(test[0])
            msg = 'test target: {}'.format(test[0])
            self.assertEqual(actual, test[1], msg)


if __name__ == "__main__":
    unittest.main()

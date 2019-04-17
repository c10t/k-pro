import unittest

#  URLify


def urlify(string, length):
    stripped = string.strip()
    assert len(stripped) == length
    return stripped.replace(' ', '%20')


class Test(unittest.TestCase):
    data = [
        {'input': ('Mr John Smith    ', 13), 'output': 'Mr%20John%20Smith'}
    ]

    def test_urlify(self):
        for test in self.data:
            actual = urlify(*test['input'])
            self.assertEqual(actual, test['output'])


if __name__ == "__main__":
    unittest.main()

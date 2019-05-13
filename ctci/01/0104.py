import unittest

# Palindrome Permutation


def palindrome(s):
    return True


class Test(unittest.TestCase):
    data = [
        ('Tact Coa', True),
        ('a', True),
        ('aa', True),
        ('ab', False),
        ('aba', True),
        ('ABCB', False),
        ('AbbA', True)
    ]

    def test_case01(self):
        pass


if __name__ == "__main__":
    unittest.main()

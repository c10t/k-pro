import unittest
from collections import Counter

#  Check Permutation


def permutation(string1, string2):
    if len(string1) != len(string2):
        return False

    c1 = Counter(string1)
    c2 = Counter(string2)

    for char in c1.keys():
        if c1[char] != c2[char]:
            return False

    return True


class Test(unittest.TestCase):
    data_T = [('abcd', 'bacd'), ('', ''), ('collect', 'letcolc')]
    data_F = [('a', 'b'), ('a', 'aa'), ('taxi', 'tax')]

    def test_permutation(self):
        # true check
        for test_string in self.data_T:
            actual = permutation(*test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.data_F:
            actual = permutation(*test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()

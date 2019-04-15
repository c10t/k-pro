import unittest

#  Is Unique


def unique(string):
    # Assume charset is ASCII (128 chars)
    if len(string) > 128:
        return False

    charset = {char for char in string}
    return len(string) == len(charset)


# with no additional data structures
def unique2(string):
    # Assume charset is ASCII (128 chars)
    if len(string) > 128:
        return False

    charset = {char for char in string}
    return len(string) == len(charset)


class Test(unittest.TestCase):
    data_T = ['abcd', 's4fad_+', '']
    data_F = ['23ds2', 'b 627h=j ()']

    def test_unique(self):
        # true check
        for test_string in self.data_T:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.data_F:
            actual = unique(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()

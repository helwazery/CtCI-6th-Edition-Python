#String Rotation: Assume you have a method isSubst ring which checks if one word is a substring
#of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
#call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").
--------------------------------------------------------------------------------------------------------------
# O(N)
import unittest


def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False


class Test(unittest.TestCase):

    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.test_cases:
            actual = string_rotation(s1, s2)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()

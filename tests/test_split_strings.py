import unittest
from split_strings import solution


class MyTestCase(unittest.TestCase):
    def test_split_strings(self):
        self.assertEqual(solution("asdfadsf"), ['as', 'df', 'ad', 'sf'])
        self.assertEqual(solution("vvdfadsf"), ['vv', 'df', 'ad', 'sf'])
        self.assertEqual(solution(""), [])


if __name__ == '__main__':
    unittest.main()

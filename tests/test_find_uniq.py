import unittest
from find_uniq import find_uniq


class MyTestCase(unittest.TestCase):
    def test_find_uniq_positive(self):
        self.assertEqual(find_uniq([2, 2, 2, 4, 2]), 4)
        self.assertEqual(find_uniq([3, 3, 3, 3, 1]), 1)
        self.assertEqual(find_uniq([10, 10, 1, 10, 10]), 1)

    # def test_find_uniq_correct_input(self):
    #     self.assertEqual(find_uniq([2, 2, 2, 4, 2]), 4)


if __name__ == '__main__':
    unittest.main()

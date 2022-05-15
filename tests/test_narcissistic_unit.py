import unittest
from narcissistic import narcissistic

class MyTestCase(unittest.TestCase):
    def test_narcissistic_good(self):
        self.assertEqual(narcissistic(371), True)
        self.assertEqual(narcissistic(153), True)
        self.assertEqual(narcissistic(7), True)

    def test_narcissistic_negative(self):
        self.assertEqual(narcissistic(4887), False)
        self.assertEqual(narcissistic(1111), False)
        self.assertEqual(narcissistic(369), False)

if __name__ == '__main__':
    unittest.main()

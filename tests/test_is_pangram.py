import unittest
from is_pangram import is_pangram

class MyTestCase(unittest.TestCase):
    def test_is_pangram_good(self):
        self.assertEqual(is_pangram('Waltz, bad nymph, for quick jigs vex.'), True)
        self.assertEqual(is_pangram('The quick, brown fox jumps over the lazy dog!'), True)
        self.assertEqual(is_pangram('Glib jocks quiz nymph to vex dwarf.'), True)



    def test_is_pangram_negative(self):
        self.assertEqual(is_pangram('sdflkvnvndjkfgjnv'), False)
        self.assertEqual(is_pangram('test'), False)
        self.assertEqual(is_pangram('1234554365f'), False)



if __name__ == '__main__':
    unittest.main()
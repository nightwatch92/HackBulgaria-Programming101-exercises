import unittest
import solution

class VowelsTest(unittest.TestCase):
    """docstring for VowelsTest"""
    def test_vowels_lower_case(self):
        self.assertEqual(6,solution.count_vowels("alaabalaa"))
        self.assertEqual(7,solution.count_vowels("Ko staaa mo stava"))
        self.assertEqual(6,solution.count_vowels("Iskam si shapkata"))
        self.assertEqual(9,solution.count_vowels("alaa blaaa blggaaa"))
        self.assertEqual(4,solution.count_vowels("albalaa"))
    def test_vowels_upper_case(self):
        self.assertEqual(6,solution.count_vowels("BABA MI E LUDA"))
        self.assertEqual(15,solution.count_vowels("AaAaAAAAAaAAAAA"))
        self.assertEqual(4,solution.count_vowels("QM SALATA SAM"))




if __name__ == '__main__':
    unittest.main()
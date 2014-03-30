import unittest
import solution

class ConsonantsTest(unittest.TestCase):
    """docstring for VowelsTest"""
    def test_consonants_lower_case(self):
        self.assertEqual(3,solution.count_consonants("alaabalaa"))
        self.assertEqual(7,solution.count_consonants("Ko staaa mo stava"))
        self.assertEqual(9,solution.count_consonants("Iskam si shapkata"))
        self.assertEqual(7,solution.count_consonants("alaa blaaa blggaaa"))
        self.assertEqual(3,solution.count_consonants("albalaa"))
    def test_consonants_upper_case(self):
        self.assertEqual(5,solution.count_consonants("BABA MI E LUDA"))
        self.assertEqual(0,solution.count_consonants("AaAaAAAAAaAAAAA"))
        self.assertEqual(7,solution.count_consonants("QM SALATA SAM"))

if __name__ == '__main__':
    unittest.main()
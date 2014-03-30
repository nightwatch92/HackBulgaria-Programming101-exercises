import unittest
import solution

class PrepareMealTest(unittest.TestCase):
    """docstring for PrepareMealTest"""

    def test_unique_words(self):
        self.assertEqual('spam spam spam ', solution.prepare_meal(27))
        self.assertEqual('spam spam and eggs', solution.prepare_meal(45))
        self.assertEqual('', solution.prepare_meal(7))
        self.assertEqual('spam ', solution.prepare_meal(3))


if __name__ == '__main__':
    unittest.main()
import unittest
import solution

class CountingWordsTest(unittest.TestCase):
    """docstring for CountingWordsTest"""
    def test_count_words(self):
        self.assertEqual({'apple': 2, 'pie': 1, 'banana': 1}, solution.count_words(['apple', 'banana', 'apple', 'pie']))
        self.assertEqual({'ruby': 1, 'python': 3}, solution.count_words(["python", "python", "python", "ruby"]))
if __name__ == '__main__':
    unittest.main()
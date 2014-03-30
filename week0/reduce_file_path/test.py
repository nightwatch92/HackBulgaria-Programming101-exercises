import unittest
import solution

class ReduceFilePathTest(unittest.TestCase):
    """docstring for ReduceFilePathTest"""

    def test_unique_words(self):
        self.assertEqual("/home/radorado/code/hackbulgaria", solution.reduce_file_path("/home//radorado/code/./hackbulgaria/week0/../"))
        self.assertEqual('/', solution.reduce_file_path("/"))
        self.assertEqual('/', solution.reduce_file_path("/srv/../"))
        self.assertEqual("/srv/www/htdocs/wtf", solution.reduce_file_path("/srv/www/htdocs/wtf/"))
        self.assertEqual('/', solution.reduce_file_path("//////////////"))


if __name__ == '__main__':
    unittest.main()
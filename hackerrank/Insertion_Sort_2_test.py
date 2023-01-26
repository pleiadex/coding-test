import unittest
from io import StringIO
from unittest.mock import patch
from Insertion_Sort_2 import insertionSort2

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
        [
            "1 4 3 5 6 2",
            "1 4 3 5 6 2\n1 3 4 5 6 2\n1 3 4 5 6 2\n1 3 4 5 6 2\n1 2 3 4 5 6\n"
        ]
    ]
  @patch('sys.stdout', new_callable = StringIO)
  def test_insertion_sort(self, stdout):
    for tc in self.testcases:
        unsorted = list(map(int, tc[0].rstrip().split()))
        insertionSort2(len(unsorted), unsorted)
        self.assertEqual(stdout.getvalue(), tc[1])

if __name__ == '__main__':
    unittest.main()
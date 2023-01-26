import unittest
from Insertion_Sort_1 import insertionSort1

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
        [
            "2 3 4 5 6 7 8 9 10 1",
            "1 2 3 4 5 6 7 8 9 10"
        ]
    ]

  def test_insertion_sort(self):
    for tc in self.testcases:
        unsorted = list(map(int, tc[0].rstrip().split()))
        sorted = list(map(int, tc[1].rstrip().split()))
        self.assertEqual(insertionSort1(len(unsorted), unsorted), sorted)

if __name__ == '__main__':
    unittest.main()
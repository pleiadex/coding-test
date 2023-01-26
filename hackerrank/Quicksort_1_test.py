import unittest
from Quicksort_1 import quickSort

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
        [
            "4 5 3 7 2",
            "3 2 4 5 7"
        ]
    ]

  def test_quick_sort(self):
    for tc in self.testcases:
        unsorted = list(map(int, tc[0].rstrip().split()))
        expect = list(map(int, tc[1].rstrip().split()))
        self.assertEqual(quickSort(unsorted), expect)

if __name__ == '__main__':
    unittest.main()
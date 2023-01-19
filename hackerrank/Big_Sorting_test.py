import unittest
from Big_Sorting import bigSorting

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      [
        ['1', '2', '100', '12303479849857341718340192371', '3084193741082937', '3084193741082938', '111', '200'],
        ['1', '2', '100', '111', '200', '3084193741082937', '3084193741082938', '12303479849857341718340192371']
      ]
    ]

  def test_big_sorting(self):
    for tc in self.testcases:
      self.assertEqual(bigSorting(tc[0]), tc[1])

if __name__ == '__main__':
    unittest.main()
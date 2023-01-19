import unittest
from Forming_a_Magic_Square import formingMagicSquare

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      [[[5, 3, 4], [1, 5, 8], [6, 4, 2]], 7],
      [[[4, 9, 2], [3, 5, 7], [8, 1, 5]], 1],
      [[[4, 4, 7], [3, 1, 5], [1, 7, 9]], 20]
    ]

  def test_forming_magic_square(self):
    for tc in self.testcases:
      self.assertEqual(formingMagicSquare(tc[0]), tc[1])

if __name__ == '__main__':
    unittest.main()
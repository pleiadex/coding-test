import unittest
from unittest.mock import patch
from io import StringIO
from Pangram import pangrams

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ['We promptly judged antique ivory buckles for the next prize', "pangram"],
      ['We promptly judged antique ivory buckles for the prize', "not pangram"],
    ]

  def test_pangrams(self):
    for tc in self.testcases:
      self.assertEqual(pangrams(tc[0]), tc[1])

if __name__ == '__main__':
    unittest.main()
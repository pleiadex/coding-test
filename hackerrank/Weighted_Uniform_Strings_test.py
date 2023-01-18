import unittest
from unittest.mock import patch
from io import StringIO
from Weighted_Uniform_Strings import weightedUniformStrings

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      [['abccddde', [1,3,12,5,9,10]], ['Yes','Yes','Yes','Yes','No','No']],
      [['aaabbbbcccddd', [9,7,8,12,5]], ['Yes','No','Yes','Yes','No']],
    ]

  def test_weighted_uniform_strings(self):
    for tc in self.testcases:
      self.assertEqual(weightedUniformStrings(*tc[0]), tc[1])

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import patch
from io import StringIO
from HackerRank_in_a_String import hackerrankInString

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ['hereiamstackerrank', "YES"],
      ['hackerworld', "NO"],
      ['hackerrankhackerrank', "YES"],
    ]

  @patch('sys.stdout', new_callable = StringIO)
  def test_hackerrank_in_string(self, stdout):

    for tc in self.testcases:
      self.assertEqual(hackerrankInString(tc[0]), tc[1])

if __name__ == '__main__':
    unittest.main()
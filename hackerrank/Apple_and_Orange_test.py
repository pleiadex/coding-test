import unittest
from unittest.mock import patch
from io import StringIO
from Apple_and_Orange import countApplesAndOranges

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      [(7, 11, 5, 15, [-2, 2, 1], [5, -6]), "1\n1\n"]
    ]

  @patch('sys.stdout', new_callable = StringIO)
  def test_count_apple_and_orange(self, stdout):

    for tc in self.testcases:
      countApplesAndOranges(*tc[0])
    self.assertEqual(stdout.getvalue(), tc[1])

if __name__ == '__main__':
    unittest.main()
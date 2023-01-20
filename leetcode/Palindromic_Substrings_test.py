import unittest
from Palindromic_Substrings import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ("abc", 3),
      ("aaa", 6),
      ("fdsklf", 6)
    ]
  def test_count_substrings(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.countSubstrings(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    